import boto3
import json

lambda_Client = boto3.client('lambda', region_name='us-east-1')
response = lambda_Client.create_function(
    Code={
        'S3Bucket': 'sr-aws-test',
        'S3Key': 'bus3.zip',  # how can i create or fetch this S3Key
    },

    FunctionName='lambda1_s3',
    Handler='bus3.lambda_handler',
    Publish=True,
    Role= 'arn:aws:iam::660836083694:role/lambda-s3' ,
    Runtime='python3.12',
)
