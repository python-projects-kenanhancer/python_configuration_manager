from .aws_config_error import AwsConfigError


class InvalidAwsRegionNameError(AwsConfigError):
    def __init__(self, message="Invalid aws region name"):
        self.message = message
        super().__init__(self.message)
