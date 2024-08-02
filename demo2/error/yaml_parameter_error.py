class YamlParameterError(Exception):
    def __init__(self, param_path: str, file_path: str):
        message = f"Parameter '{param_path}' not found in YAML file '{file_path}' and no default value provided."
        super().__init__(message)
        self.param_path = param_path
        self.file_path = file_path
