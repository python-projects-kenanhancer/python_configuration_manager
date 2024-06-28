import logging
from enum import Enum
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

logging.basicConfig(level=logging.INFO)


class AwsService(Enum):
    S3 = "s3"
    EC2 = "ec2"
    LAMBDA = "lambda"
    DYNAMODB = "dynamodb"
    SNS = "sns"
    SQS = "sqs"
    SSM = "ssm"


class AwsConfig:
    def __init__(
        self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str
    ):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self._session = None
        self._validate_config()

    def _validate_config(self) -> None:
        if not all(
            [self.aws_access_key_id, self.aws_secret_access_key, self.region_name]
        ):
            raise ValueError(
                "AWS access key, secret access key, and region name must be provided"
            )

    def _session_exists(self) -> bool:
        return self._session is not None

    def _initialize_session(self) -> None:
        if not self._session_exists():
            try:
                self._session = boto3.Session(
                    aws_access_key_id=self.aws_access_key_id,
                    aws_secret_access_key=self.aws_secret_access_key,
                    aws_session_token=self.region_name,
                )
                logging.info("AWS session created successfully")
            except (NoCredentialsError, PartialCredentialsError) as e:
                logging.error(f"Error creating AWS session: {e}")
                raise

    @property
    def session(self) -> boto3.Session:
        self._initialize_session()
        return self._session

    def create_client(self, service_name: AwsService) -> boto3.client:
        try:
            client = self.session.client(service_name.value)
            logging.info(f"AWS client for {service_name} service created successfully")
            return client
        except ClientError as e:
            logging.error(f"Error creating client for AWS {service_name} service: {e}")
            raise
