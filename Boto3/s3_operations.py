#functions to use CRUD operations on S3 buckets using boto3
import boto3
from botocore.exceptions import ClientError

#create an S3 client
s3 = boto3.client("s3")

#create an S3 bucket
def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created.")
        return True

    except ClientError as e:
        print(e)
        return False
    
#S3 Read operations - with options to list buckets and list objects in a bucket
#List all buckets in S3
def list_buckets():
    response = s3.list_buckets()
    return response["Buckets"]

#List all objects in a specific bucket

def list_objects(bucket_name):
    """
    Returns a list of objects in the specified bucket.
    """

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        return response.get("Contents", [])

    except ClientError as e:
        print(f"Error reading bucket '{bucket_name}': {e}")
        return []
    

#read the contents of an object in a bucket TODO: implement this function

#delete an S3 bucket
def delete_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted.")
        return True

    except ClientError as e:
        print(e)
        return False
    

