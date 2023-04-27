python
import boto3
import requests
import json

def download_data():
    # download data from GOES satellite
    response = requests.get('https://www.goes.gov/data/')
    if response.status_code == 200:
        # save the data to S3 bucket
        s3 = boto3.client('s3')
        s3.put_object(Bucket='my_bucket', Key='GOES_satellite_data')
    else:
        print('Error: Failed to download data from GOES satellite.')
