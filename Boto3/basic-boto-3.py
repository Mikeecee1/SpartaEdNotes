import boto3
import pprint as pp

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

# bucket_list = s3_client.list_buckets()
# for bucket in bucket_list['Buckets']:
#     print(bucket['Name'])

# List all objects in a bucket
# bucket_name = "data-eng-resources"
# bucket_contents = s3_client.list_objects_v2(
#   Bucket=bucket_name
#   )
# for object in bucket_contents['Contents']:
#     print(object['Key'])
bucket_name = "data-eng-resources"
    # Get object contents from s3
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key="python/chatbot-intent.json"
)
pp.pprint(s3_object, sort_dicts=False)