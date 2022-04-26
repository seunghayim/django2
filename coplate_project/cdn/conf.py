import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = "https://langhae.s3.eu-west-2.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}

AWS_LOCATION = "https://langhae.s3.eu-west-2.amazonaws.com"
DEFAULT_FILE_STORAGE = "coplate_project.cdn.backends.MediaStorage"
STATICFILES_STORAGE = "coplate_project.cdn.backends.StaticStorage"
# https: // langhae.s3.eu-west-2.amazonaws.com/static/admin/css/autocomplete.css
