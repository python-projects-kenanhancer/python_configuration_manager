from functools import lru_cache, wraps
import json
import logging
import boto3
from botocore.exceptions import ClientError

from error.aws_secret_parameter_error import AwsSecretParameterError


_aws_secrets = {}
_aws_secret_manager_client = boto3.client("secretsmanager")


@lru_cache()
def _get_aws_secret(secret_name: str, key: str, default_value: str | None = None):
    if secret_name not in _aws_secrets:
        try:
            response = _aws_secret_manager_client.get_secret_value(SecretId=secret_name)
            secret_string = response["SecretString"]
            secret_dict = json.loads(secret_string)
            _aws_secrets[secret_name] = secret_dict
            value = secret_dict.get(key, default_value)
            return value
        except ClientError as e:
            logging.error("Error getting secret %s: %s", secret_name, e)
            return default_value
        except json.JSONDecodeError as e:
            logging.error("Error decoding JSON for secret %s: %s", secret_name, e)
            return default_value

    value = _aws_secrets[secret_name].get(key, default_value)
    return value


def aws_secret_parameter(secret_name: str, key: str, default_value: str | None = None):
    def decorator(func):
        @property
        @wraps(func)
        def wrapper(instance):
            property_name = func.__name__
            attribute_name = f"_{func.__name__}_cached_value"
            if not hasattr(instance.__class__, attribute_name):
                value = _get_aws_secret(secret_name, key, default_value)
                if value is None:
                    raise AwsSecretParameterError(secret_name, key, property_name)
                setattr(instance.__class__, attribute_name, value)
            return getattr(instance.__class__, attribute_name)

        return wrapper

    return decorator
