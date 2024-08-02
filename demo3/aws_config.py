from error import (
    InvalidAwsAccessKeyIdError,
    InvalidAwsSecretAccessKeyError,
    InvalidAwsRegionNameError,
)


class AwsConfig:
    def __init__(
        self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str
    ):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name

    def _validate_aws_access_key_id(self, value: str):
        if not value or not isinstance(value, str):
            raise InvalidAwsAccessKeyIdError()

    def _validate_aws_secret_access_key(self, value: str):
        if not value or not isinstance(value, str):
            raise InvalidAwsSecretAccessKeyError()

    def _validate_region_name(self, value: str):
        if not value or not isinstance(value, str):
            raise InvalidAwsRegionNameError()

    @property
    def aws_access_key_id(self):
        return self._aws_access_key_id

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: str):
        self._validate_aws_access_key_id(value)
        self._aws_access_key_id = value

    @property
    def aws_secret_access_key(self):
        return self._aws_secret_access_key

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: str):
        self._validate_aws_secret_access_key(value)
        self._aws_secret_access_key = value

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value: str):
        self._validate_region_name(value)
        self._region_name = value
