#functions to use CRUD operations on S3 buckets using boto3
import boto3
from botocore.exceptions import ClientError

#create an S3 client not needed for testing purposes
#s3 = boto3.client("s3")
#Fake data for testing purposes without AWS S3 connection
# Fake bucket data
fake_buckets = [
    {"Name": "sparta-training"},
    {"Name": "web-app-assets"},
    {"Name": "customer-backups"},
    {"Name": "project-data"},
    {"Name": "test-bucket"},
]

# Fake object data
fake_objects = {
    "sparta-training": [
        {"Key": "lesson1.pdf", "Size": 24576},
        {"Key": "lesson2.pdf", "Size": 28342},
    ],
    "web-app-assets": [
        {"Key": "logo.png", "Size": 45231},
        {"Key": "banner.jpg", "Size": 192384},
    ],
    "test-bucket": [],
}
#create an S3 bucket vetrsion for testing purposes
def create_bucket(bucket_name):
    fake_buckets.append({"Name": bucket_name})
    fake_objects[bucket_name] = []
    print(f"Created bucket '{bucket_name}'")
    
#S3 Read operations - with options to list buckets and list objects in a bucket
#List all buckets in S3 #dummy data for testing purposes
def list_buckets():
    return fake_buckets

    # Uncomment on Monday
    # response = s3.list_buckets()
    # return response["Buckets"]

#List all objects in a specific bucket -dummy version for testing purposes

def list_objects(bucket_name):
    return fake_objects.get(bucket_name, [])

    # Uncomment on Monday
    # response = s3.list_objects_v2(Bucket=bucket_name)
    # return response.get("Contents", [])
    

#read the contents of an object in a bucket TODO: implement this function

#delete an S3 bucket version for testing purposes

def delete_bucket(bucket_name):
    for bucket in fake_buckets:
        if bucket["Name"] == bucket_name:
            fake_buckets.remove(bucket)
            break

    fake_objects.pop(bucket_name, None)

    print(f"Deleted bucket '{bucket_name}'")