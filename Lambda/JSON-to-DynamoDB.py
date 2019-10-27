#Uploading JSON content to DynamoDB table in AWS

#Import modules
import json
import urllib.parse
import boto3
import csv

s3 = boto3.client('s3')

def lambda_handler(event, context):

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    textract_json = event['Records'][0]['s3']['object']['key']
    textract_json_obj=s3.get_object(Bucket=bucket,Key=textract_json)
    FileReader = textract_json_obj['Body'].read()
    TT_Dict = json.loads(FileReader)
    #The DynamoDB table in this example is assumed to be called DynamoTable
    table = boto3.resource('dynamodb').Table('DynamoTable')
    table.put_item(Item=TT_Dict)
