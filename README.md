# AWS Text Comprehension, Form Extraction, and Databasing through Lambda and Textract
In this code, we will be using AWS S3, AWS Textract, AWS DynamoDB, and AWS Lambda to extract forms from a JPEG/PNG image and
upload its contents into a NOSQL dababase.

# Proposed Architecture
The core components of this projects are utilised in the architecture below.


![Proposed Architecture](https://github.com/ghaithfarfour/AWS-Forms-Extraction-and-Databasing/blob/master/Architecture.png)

# Lambda Functions
Two Lambda functions were written for this process.

1. S3 to JSON
This Lambda function uses the analyze_document function from AWS Textract to extract the forms from an uploaded S3 image. The return of 
this function is a JSON file with contain key-value pairs of the forms, as well as a URL to the image location in the S3 Bucket.

2. JSON to DDB
Once a JSON file is resulted from the S3-to-JSON function, this function populates the output into a pre-created DynamoDB database.

