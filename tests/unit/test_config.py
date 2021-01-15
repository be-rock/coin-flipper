import os

from coin_flipper.settings import get_app_config, set_app_env_vars


def test_app_config_reader(tmp_path):
    """
    sample yaml file for tests:
    a:
      b
    c:
      - x
      - y
    """
    content = "a: \n  b\nc:\n  - x \n  - y\n"
    p = tmp_path / "config.yaml"
    p.write_text(content)
    config = get_app_config()
    assert all([k in ["a", "b"] for k in config])
    assert isinstance(config, dict)


def test_env_setter(tmp_path):
    """
    sample .env file for tests:
    k1=v1
    k2=v2
    """
    content = "k1=v1\nk2=v2"
    p = tmp_path / "config.yaml"
    p.write_text(content)
    set_app_env_vars(p.absolute())
    assert os.getenv("k1") == "v1"
    assert os.getenv("k2") == "v2"
