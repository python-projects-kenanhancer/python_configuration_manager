from aws_config import AwsConfig


if __name__ == "__main__":
    aws_config = AwsConfig(
        "your_access_key_id", "your_secret_access_key", "your_region"
    )

    print(aws_config.aws_access_key_id)
    print(aws_config.aws_secret_access_key)
    print(aws_config.region_name)
