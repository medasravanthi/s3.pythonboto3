import boto3
import json

def lambda_handler(event,context) :
    client = boto3.client('s3',region_name='us-east-1')
    response = client.create_bucket(
    Bucket='us-s3-hyd'
   )
