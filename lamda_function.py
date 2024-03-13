import boto3
import pandas as pd
from datetime import datetime
import os

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_arn = os.getenv('SNS_ARN')  
target_bucket_name = os.getenv('TARGET_BUCKET_NAME')


def lambda_handler(event, context):
    # Format today's date
    today = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    target_file_key = f'{today}-processed.json'

    # TODO implement
 
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_file_key = event["Records"][0]["s3"]["object"]["key"]

        resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_key)
        # print(resp['Body'])
        df_s3_data = pd.read_json(resp['Body'])
        # print(df_s3_data.head().to_json(orient='records', lines=True))

        filtered_data = df_s3_data.loc[df_s3_data['status'] == "delivered"]

        # Convert the filtered DataFrame to a JSON string
        filtered_json_str = filtered_data.to_json(orient='records')
        
        # Convert the JSON string to bytes
        filtered_json_bytes = filtered_json_str.encode('utf-8')

        # Write the bytes to S3
        s3_client.put_object(Bucket=target_bucket_name, Key=target_file_key, Body=filtered_json_bytes)

        message = "Input S3 File {} has been processed succesfuly !!".format("s3://"+bucket_name+"/"+s3_file_key)
        respone = sns_client.publish(Subject="SUCCESS - Daily Data Processing",TargetArn=sns_arn, Message=message, MessageStructure='text')
    except Exception as err:
        print(err)
        message = "Input S3 File {} processing is Failed !!".format("s3://"+bucket_name+"/"+s3_file_key)
        respone = sns_client.publish(Subject="FAILED - Daily Data Processing", TargetArn=sns_arn, Message=message, MessageStructure='text')