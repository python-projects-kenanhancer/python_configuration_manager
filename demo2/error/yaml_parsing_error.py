class YamlParsingError(Exception):
    def __init__(self, file_path: str, original_exception: Exception):
        message = f"Error parsing YAML file '{file_path}': {original_exception}"
        super().__init__(message)
        self.file_path = file_path
        self.original_exception = original_exception
