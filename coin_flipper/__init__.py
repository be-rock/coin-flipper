from .settings import APP_ENV, get_app_config, get_logger, set_app_env_vars

set_app_env_vars()
CONFIG = get_app_config()
