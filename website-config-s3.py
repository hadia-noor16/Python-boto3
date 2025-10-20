import boto3
import json

s3=boto3.client('s3')
bucket_name='hadia-doing-boto3demo'

for key in ("index.html","error.html", "coffee.jpg"):
    s3.upload_file(key, bucket_name,key)


website_config = {
    'ErrorDocument' : {'Key' : 'error.html'},
    'IndexDocument' : {'Suffix' : 'index.html'}
}

s3.put_bucket_website(Bucket=bucket_name,WebsiteConfiguration=website_config)

s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False,
    },
)

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicReadForWebsite",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"],
        }
    ],
}

s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))