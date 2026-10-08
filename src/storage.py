import boto3

# This value won't be auto-detected by the scanner — we'll use Teach to mark it
COMPANY_INTERNAL_ID = "~[PREFIXED_CUSTOMER_ID_0]~"

s3 = boto3.client(
    's3',
    aws_access_key_id='~[AWS_ACCESS_KEY_ID_0]~',
    aws_secret_access_key='~[AWS_SECRET_KEY_0]~',
    region_name='us-east-1'
)

def upload(bucket: str, key: str, data: bytes):
    s3.put_object(Bucket=bucket, Key=key, Body=data)
