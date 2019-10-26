#Loading AWS CLI and Packages
import os
import os.path
import sys
import boto3
import json
import csv
import sys
import urllib.parse
from trp import Document

print('Loading function')

#S3 and textract clients
s3 = boto3.resource('s3')
s3client = boto3.client('s3')
textract = boto3.client('textract')

def invokeTextract(bucketName, documentKey):
    print('Loading invokeTextract')
    # Call Amazon Textract
    response = textract.analyze_document(Document={'S3Object': {'Bucket': bucketName,'Name': documentKey}},FeatureTypes=["FORMS"])
    
    document = Document(response)

    return document

def outputForm(page):
    csvData = []
    for field in page.form.fields:
        csvItem  = []
        if(field.key):
            csvItem.append(field.key.text)
        else:
            csvItem.append("-")
        if(field.value):
            csvItem.append(field.value.text)
        else:
            csvItem.append("-")
        csvData.append(csvItem)
    return csvData

def writeTextractToS3File(forms_json, bucketName, createdS3Document):
    print('Loading writeTextractToS3File')
    generateFilePath = os.path.splitext(createdS3Document)[0] + '.json'
    print('File Path Generated')
    s3client.put_object(Body=bytes(json.dumps(forms_json).encode('UTF-8')), Bucket=bucketName, Key=generateFilePath)
    print('Generated ' + generateFilePath)

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("key is "+key)
    print("bucket is "+bucket)
    
    location = boto3.client('s3').get_bucket_location(Bucket=bucket)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket, key)
    
    print (url)
    
    try:
        document = invokeTextract(bucket,key)
        print("Textract Invoked")
        forms={}
        #print(document)
        for page in document.pages:
            forms = outputForm(page)
        print (forms)
        forms_dict = dict(forms)
        forms_dict['url'] = url
        print (forms_dict)
        writeTextractToS3File(forms_dict, bucket, key)
        
        return 'Processed'
        
    except Exception as e:
        print(e)
        print('Error: ')
        raise ePropo
