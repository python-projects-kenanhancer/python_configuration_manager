import os
from decorators import (
    aws_ssm_parameter,
    aws_secret_parameter,
    env_parameter,
    yaml_file_parameter,
)


class Config:
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

    @aws_ssm_parameter(name="/myapp/api_key", default_value="default_api_key")
    def api_key(self):
        pass

    @aws_ssm_parameter(name="/myapp/db_host", default_value="default_db_host")
    def db_host(self):
        pass

    @aws_ssm_parameter(name="/myapp/db_name", default_value="default_db_name")
    def db_name(self):
        pass

    @aws_secret_parameter(
        secret_name="/myapp/secret",
        key="db_password",
        default_value="default_db_password",
    )
    def db_password(self):
        pass

    @aws_secret_parameter(
        secret_name="/myapp/secret", key="db_user", default_value="default_db_user"
    )
    def db_user(self):
        pass

    @env_parameter(env_name="MYAPP_API_KEY", default_value="env_default_api_key")
    def env_api_key(self):
        pass

    @yaml_file_parameter(config_path, "database.main.url")
    def database_url(self):
        pass

    @yaml_file_parameter(config_path, "database.main.timeout", default_value=10)
    def database_timeout(self):
        pass

    @yaml_file_parameter(config_path, "database.main.replicas")
    def database_replicas(self):
        pass

    @yaml_file_parameter(config_path, "api.keys.service1")
    def service1_api_key(self):
        pass

    @yaml_file_parameter(config_path, "api.keys.service2")
    def service2_api_key(self):
        pass

    @yaml_file_parameter(config_path, "api.endpoints")
    def api_endpoints(self):
        pass

    @yaml_file_parameter(config_path, "api.endpoints.0.path")
    def first_endpoint_path(self):
        pass
    
    @yaml_file_parameter(config_path, "api.endpoints.0.path")
    def first_endpoint_path2(self):
        pass

    @yaml_file_parameter(config_path, "api.endpoints.0.timeout")
    def first_endpoint_timeout(self):
        pass
