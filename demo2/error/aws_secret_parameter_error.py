class AwsSecretParameterError(Exception):
    def __init__(self, secret_name: str, key: str, property_name: str):
        message = (
            f"AWS Secret '{secret_name}' does not contain key '{key}' for property '{property_name}' "
            "and no default value was provided."
        )
        super().__init__(message)
        self.secret_name = secret_name
        self.key = key
        self.property_name = property_name
