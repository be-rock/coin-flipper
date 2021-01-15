import os
from pathlib import Path

import yaml

APP_ENV = os.environ.get("APP_ENV", "dev")  # dev, tst, prd
DEBUG = True if os.environ.get("DEBUG", "").lower().startswith("y") else False


def get_config_path(file_name: str) -> Path:
    """
       path helper for config files that allows relative
       or absolute paths to be passed as an arg
    """
    return (
        Path(file_name)
        if Path(file_name).is_absolute()
        else Path(__file__).parent / file_name
    )


def get_app_config(config_file: str = "app-conf.yaml") -> dict:
    p = get_config_path(config_file)
    with open(p.absolute()) as y:
        return yaml.safe_load(y)


def set_app_env_vars(env_file: str = ".env") -> None:
    p = get_config_path(env_file)
    with open(p.absolute(), "r") as f:
        data = f.read()
        for item in data.rstrip("\n").split("\n"):
            k, v = item.split("=")
            os.environ[k] = v
