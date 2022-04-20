import os

AWS_ACCESS_KEY_ID = os.getenv("DO_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("DO_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("DO_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}

AWS_LOCATION = "https://langhae.nyc3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "coplate_project.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "coplate_project.cdn.backends.StaticRootS3BotoStorage"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
