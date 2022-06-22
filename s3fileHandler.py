from http import client
from secrets import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

def uploadToS3(file):
    if '.csv' in file:
        upload_file_bucket = 'sarvm-poc-bucket'
        upload_file_key = str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)