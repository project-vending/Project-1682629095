
import boto3

s3 = boto3.resource('s3')

def upload_to_s3(bucket_name, file_path, object_name):
    """
    Upload a file to an S3 bucket
    :param bucket_name: str
    :param file_path: str
    :param object_name: str
    :return: bool
    """
    try:
        s3.meta.client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading object {object_name} to S3 bucket {bucket_name}: {e}")
        return False
    
    print(f"Uploaded {object_name} to S3 bucket {bucket_name}")
    return True
