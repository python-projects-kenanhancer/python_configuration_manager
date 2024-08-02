class AwsSsmParameterError(Exception):
    def __init__(self, name: str):
        message = f"AWS Ssm '{name}' not found and no default value provided."
        super().__init__(message)
        self.name = name
