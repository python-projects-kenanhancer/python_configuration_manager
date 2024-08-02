import os
from functools import wraps

from error.env_variable_error import EnvVariableError


def _get_env_value(env_name: str, default_value: str | None = None):
    value = os.getenv(env_name, default_value)
    if value is None:
        raise EnvVariableError(env_name)
    return value


def env_parameter(env_name: str, default_value: str | None = None):
    def decorator(func):
        @property
        @wraps(func)
        def wrapper(instance):
            attribute_name = f"_{func.__name__}_cached_value"
            if not hasattr(instance.__class__, attribute_name):
                value = _get_env_value(env_name, default_value)
                setattr(instance.__class__, attribute_name, value)
            return getattr(instance.__class__, attribute_name)

        return wrapper

    return decorator
