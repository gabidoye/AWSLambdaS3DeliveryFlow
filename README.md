# AWSLambdaS3DeliveryFlow

Automated AWS Solution for DoorDash Delivery Data Processing
Overview
This project develops an automated solution leveraging AWS services to process daily delivery data from DoorDash. The process involves uploading JSON files containing delivery records to an Amazon S3 bucket. An AWS Lambda function, triggered by these uploads, filters the records based on their delivery status. The filtered data is then saved to a separate S3 bucket. Amazon Simple Notification Service (SNS) is used to send notifications about the processing outcome.

## Requirements
AWS Account
Amazon S3 Buckets: Two buckets are required, doordash-bronze-zn for incoming raw files and doordash-gold-zn for processed files.
AWS Lambda: For executing the data processing script.
Amazon SNS: For sending notifications regarding the processing outcome.
AWS IAM: To manage permissions for accessing AWS resources.
AWS CodeBuild: For continuous integration and deployment (CI/CD) purposes.
GitHub: For version control.
Python & pandas library: The Lambda function is written in Python, utilizing the pandas library for data manipulation.
Email Subscription: For receiving SNS notifications.

## Implementation Steps
Sample Data
A sample JSON file named 2024-03-09-raw_input.json contains 1000 delivery records with various statuses (e.g., cancelled, delivered, order placed).

Example record:

json
Copy code
{"id": 1, "status": "delivered", "amount": 20.5, "date": "2024-03-09"}

## Process Flow
S3 Buckets Setup: Create doordash-landing-zn and doordash-target-zn buckets.
Amazon SNS Topic Setup: Create an SNS topic for notifications and subscribe an email to receive these notifications.
IAM Role Creation: Set up an IAM role with permissions tailored for reading from the landing bucket, writing to the target bucket, and publishing messages to the SNS topic.
AWS Lambda Configuration: Deploy a Python-based Lambda function with pandas. It triggers on file uploads to doordash-bronze-zn, filters records with "delivered" status, and writes the output to doordash-gold-zn.
CI/CD with AWS CodeBuild: Link your GitHub repository containing the Lambda function code to AWS CodeBuild. Automate deployments using buildspec.yml.

<img width="1187" alt="image" src="https://github.com/gabidoye/AWSLambdaS3DeliveryFlow/assets/86935340/d164172f-9edf-498c-8e77-0b6c9a7c0efc">


## Testing & Verification: 
Upload a sample JSON to doordash-bronze-zn to trigger the Lambda function. Verify the processed file in doordash-gold-zn and check for the email notification confirming the process completion.

## Getting Started
To replicate this solution, ensure you have all the requirements in place. Follow the implementation steps outlined above to set up the environment, configure AWS services, and deploy your function.


I warmly welcome contributions, feedback, and suggestions from the community! Whether you're interested in improving the code, suggesting new features, or reporting bugs, your input is valuable in making this project more effective and versatile.
