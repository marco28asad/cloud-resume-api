# cloud-resume-api
Serverless REST API built with AWS Lambda and API Gateway that serves resume data as JSON


# Cloud Resume API

A serverless REST API built on AWS that serves live resume data as JSON.

## Live API
https://iid8drt6u8.execute-api.us-east-2.amazonaws.com/hello

## Built With
- AWS Lambda
- AWS API Gateway
- Python 3.12

## Architecture
Client sends a GET request to the API Gateway endpoint. API Gateway triggers the Lambda function. Lambda processes the request and returns JSON data with a 200 status code.

## Features
- Serverless architecture with zero server management
- REST API with proper HTTP status codes
- JSON response format
- Auto-scaling and pay-per-request pricing model

## How To Use
Send a GET request to the live API endpoint:

    curl https://iid8drt6u8.execute-api.us-east-2.amazonaws.com/hello

## What I Learned
- Deploying and configuring AWS Lambda functions
- Creating and connecting HTTP APIs with API Gateway
- Serverless architecture patterns
- Python for cloud functions
- AWS IAM permissions and resource policies
