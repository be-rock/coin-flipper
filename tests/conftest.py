import pytest

from src.adapters.repository import FakeRepository
from src.domain.model import Coin


@pytest.fixture()
def coin_fixture():
    yield Coin(number_of_flips=10)


@pytest.fixture()
def fake_repository_fixture():
    yield FakeRepository()



