from .aws_config_error import AwsConfigError


class InvalidAwsAccessKeyIdError(AwsConfigError):
    def __init__(self, message="Invalid aws access key id"):
        self.message = message
        super().__init__(self.message)
