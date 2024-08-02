from config import Config


if __name__ == "__main__":
    config = Config()

    print(config.env_api_key)

    print(config.db_password)

    print(config.first_endpoint_path)

    print(config.first_endpoint_path2)

    print(config.first_endpoint_timeout)

    print("Done.")
