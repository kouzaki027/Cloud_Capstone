import boto3
import uuid

# Credentials:
# after pasting your Access key ID and Secret access key, uncomment lines 6 through 11
#s3_resource = boto3.resource('s3',
#         aws_access_key_id='xyz',
#         aws_secret_access_key='xyz')
#s3_client = boto3.client('s3',
#         aws_access_key_id='xyz',
#         aws_secret_access_key='xyz')

# retrieve the list of existing buckets
response = s3_client.list_buckets()
count = 1 
# output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print ( count ) 
    print(f'  {bucket["Name"]}')
    count = count+1                         
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
# bucket prefix CANNOT be uppercase nor spaces; they can only contain lowercase letters, hyphens (-), and numbers
bucket_prefix='jrd'
BN = ''.join([bucket_prefix, str(uuid.uuid4())])
print ( "New Bucket about to be created:   " ,BN)
print(' ')




# Creating buckets:
s3_resource.create_bucket(Bucket=BN,
                          CreateBucketConfiguration={
                              'LocationConstraint': 'us-east-2'})
# note, bucket names must be unique




# Retriving the existing buckets:
response = s3_client.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')





# Updating the existing buckets:
first_file_name='timestampText.txt'
s3_resource.Object(BN, first_file_name).upload_file(
    Filename=first_file_name)
