import os
from functools import lru_cache, wraps
import yaml

from error import YamlParameterError, YamlParsingError


@lru_cache(maxsize=None)
def _load_yaml_file(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YAML file '{file_path}' does not exist.")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise YamlParsingError(file_path, e) from e


def _get_nested_value(data, param_path: str, default_value: str | None = None):
    """Retrieve a nested value from a dictionary using a dot-separated path."""
    keys = param_path.split(".")
    value = data
    try:
        for key in keys:
            if isinstance(value, list):
                key = int(key)  # Convert to integer if the current value is a list
            value = value[key]
    except (KeyError, IndexError, ValueError):
        value = default_value

    if value is None:
        raise YamlParameterError(param_path, data)

    return value


_yaml_path_cache = {}


def yaml_file_parameter(
    file_path: str, param_path: str, default_value: str | None = None
):

    def decorator(func):
        @property
        @wraps(func)
        def wrapper(instance):
            attribute_name = f"_{func.__name__}_cached_value"
            if not hasattr(instance.__class__, attribute_name):
                if file_path not in _yaml_path_cache:
                    _yaml_path_cache[file_path] = {}
                if param_path not in _yaml_path_cache[file_path]:
                    yaml_content = _load_yaml_file(file_path)
                    value = _get_nested_value(yaml_content, param_path, default_value)
                    _yaml_path_cache[file_path][param_path] = value
                setattr(
                    instance.__class__,
                    attribute_name,
                    _yaml_path_cache[file_path][param_path],
                )
            return getattr(instance.__class__, attribute_name)

        return wrapper

    return decorator
