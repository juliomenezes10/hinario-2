import boto3
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def upload_to_s3(file):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )
    
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_name = file.name
    file_content = file.read()

    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content,
        ContentType='audio/mpeg'
    )
