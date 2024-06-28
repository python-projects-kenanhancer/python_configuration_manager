import logging
from aws_config import AwsConfig, AwsService
from botocore.exceptions import ClientError


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # AWS credentials and region for the first account
    AWS_ACCESS_KEY_ID_1 = "your_access_key_id_1"
    AWS_SECRET_ACCESS_KEY_1 = "your_secret_access_key_1"
    REGION_NAME_1 = "your_region_1"

    # AWS credentials and region for the second account
    AWS_ACCESS_KEY_ID_2 = "your_access_key_id_2"
    AWS_SECRET_ACCESS_KEY_2 = "your_secret_access_key_2"
    REGION_NAME_2 = "your_region_2"

    aws_config_1 = None  # pylint: disable=invalid-name
    aws_config_2 = None  # pylint: disable=invalid-name
    s3_client_1 = None  # pylint: disable=invalid-name
    s3_client_2 = None  # pylint: disable=invalid-name

    try:
        aws_config_1 = AwsConfig(
            AWS_ACCESS_KEY_ID_1, AWS_SECRET_ACCESS_KEY_1, REGION_NAME_1
        )
        logging.info("AWS config for first account initialized successfully")
    except ValueError as e:
        logging.error(f"Error initializing AWS config for first account: {e}")

    try:
        aws_config_2 = AwsConfig(
            AWS_ACCESS_KEY_ID_2, AWS_SECRET_ACCESS_KEY_2, REGION_NAME_2
        )
        logging.info("AWS config for second account initialized successfully")
    except ValueError as e:
        logging.error(f"Error initializing AWS config for second account: {e}")

    # Create an AWS S3 client for the first account if aws_config_1 was initialized
    if aws_config_1:
        try:
            s3_client_1 = aws_config_1.create_client(AwsService.S3)
            logging.info("AWS S3 client for first account created successfully")
        except ClientError as e:
            logging.error(f"Error creating AWS S3 client for first account: {e}")

    # Create an AWS S3 client for the second account if aws_config_2 was initialized
    if aws_config_2:
        try:
            s3_client_2 = aws_config_2.create_client(AwsService.S3)
            logging.info("AWS S3 client for second account created successfully")
        except ClientError as e:
            logging.error(f"Error creating AWS S3 client for second account: {e}")

    # List AWS S3 buckets for the first account if s3_client_1 was created successfully
    if s3_client_1:
        try:
            s3_bucket_list_1 = s3_client_1.list_buckets()
            logging.info(f"Buckets in first account: {s3_bucket_list_1['Buckets']}")
        except ClientError as e:
            logging.error(f"Failed to list buckets in first account: {e}")

    # List AWS S3 buckets for the second account if s3_client_2 was created successfully
    if s3_client_2:
        try:
            s3_bucket_list_2 = s3_client_2.list_buckets()
            logging.info(f"Buckets in second account: {s3_bucket_list_2['Buckets']}")
        except ClientError as e:
            logging.error(f"Failed to list buckets in second account: {e}")
