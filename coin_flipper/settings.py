import logging
import os
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import yaml

APP_ENV = os.environ.get("APP_ENV", "dev")  # dev, tst, prd
DEBUG = True if os.environ.get("DEBUG", "").lower().startswith("y") else False
LOG_FILE = "app.log"
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT)
LOG_ROTATE_TIME = "midnight"
LOG_HOME = os.getenv("LOG_DIR", "/tmp")


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
    """app config (yaml) reader"""
    p = get_config_path(config_file)
    with open(p.absolute()) as y:
        return yaml.safe_load(y)


def set_app_env_vars(env_file: str = ".env") -> None:
    """dotenv config reader"""
    p = get_config_path(env_file)
    with open(p.absolute(), "r") as f:
        data = f.read()
        for item in data.rstrip("\n").split("\n"):
            k, v = item.split("=")
            os.environ[k] = v


def get_timed_file_handler(
    log_dir: str = LOG_HOME,
    log_file: str = LOG_FILE,
    log_rotate_time: str = LOG_ROTATE_TIME,
    backup_count=None,
):
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, log_file), when=log_rotate_time, backupCount=backup_count
    )
    file_handler.setFormatter(LOG_FORMATTER)
    return file_handler


def get_logger(
    logger_name: str,
    level=LOG_LEVEL,
    handler: logging.handlers = get_timed_file_handler(),
):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
