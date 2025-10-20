import boto3
import json

# Initialize an S3 client
s3 = boto3.client('s3')
bucket_name='hadia-doing-boto3demo'
region='us-east-1'

 #Create a new S3 bucket with the specified name 'hadia-doing-boto3demo'
response = s3.create_bucket(
    Bucket=bucket_name
)
#print(response)

# upload objects

s3.upload_file('./hello.txt', bucket_name, 'hello.txt')
