from .aws_config_error import AwsConfigError


class InvalidAwsSecretAccessKeyError(AwsConfigError):
    def __init__(self, message="Invalid aws secret access key"):
        self.message = message
        super().__init__(self.message)
