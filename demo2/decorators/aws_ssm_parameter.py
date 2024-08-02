from functools import lru_cache, wraps
import logging
import boto3
from botocore.exceptions import ClientError

from error.aws_ssm_parameter_error import AwsSsmParameterError

_aws_ssm_client = boto3.client("ssm")


@lru_cache()
def _get_aws_ssm_parameter(name: str, default_value: str | None):
    try:
        response = _aws_ssm_client.get_parameter(Name=name, WithDecryption=True)
        return response["Parameter"]["Value"]
    except ClientError as e:
        logging.error("Error retrieving AWS SSM parameter %s: %s", name, e)
        return default_value
    except KeyError as e:
        logging.error(
            "Unexpected response structure when retrieving AWS SSM parameter %s: %s",
            name,
            e,
        )
        return default_value


def aws_ssm_parameter(name: str, default_value: str | None = None):
    def decorator(func):
        @property
        @wraps(func)
        def wrapper(instance):
            attribute_name = f"_{func.__name__}_cached_value"
            if not hasattr(instance.__class__, attribute_name):
                value = _get_aws_ssm_parameter(name, default_value)
                if value is None:
                    raise AwsSsmParameterError(name)
                setattr(instance.__class__, attribute_name, value)
            return getattr(instance.__class__, attribute_name)

        return wrapper

    return decorator
