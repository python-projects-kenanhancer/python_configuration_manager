class EnvVariableError(Exception):
    def __init__(self, env_name: str):
        message = f"Environment variable '{env_name}' not found and no default value provided."
        super().__init__(message)
        self.env_name = env_name
