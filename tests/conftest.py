import pytest

from src.domain.model import Coin


@pytest.fixture()
def test_coin_fixture():
    yield Coin(number_of_flips=10)
