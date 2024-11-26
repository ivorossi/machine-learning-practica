import toml


class Config:
    _config = None
    _default_path = "src/main/resources/config.toml"
    _default_database = "my_configurations"

    @staticmethod
    def _load_default():
        if Config._config is None:
            Config._config = toml.load(Config._default_path)

    @staticmethod
    def set_config_path_and_database(toml_path, database_name):
        Config._default_path = toml_path
        Config._default_database = database_name

    @staticmethod
    def get_config():
        Config._load_default()
        return Config._config.get(Config._default_database)
