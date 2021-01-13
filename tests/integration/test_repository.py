import pytest
from sqlalchemy import select

from src.domain.model import Coin, CoinFlipResult

pytestmark = pytest.mark.usefixtures("mappers")


def test_sqlalchemy_repository_create_coinflip_model_item(sqlalchemy_on_disk_fixture):
    repo = sqlalchemy_on_disk_fixture
    flip_num = 10
    coin = Coin()
    results = coin.flip(number_of_flips=flip_num)
    flip_model_obj = CoinFlipResult(
        number_of_flips=flip_num, flip_results=dict(results)
    )
    repo.add(flip_model_obj)
    stmt = select(CoinFlipResult)
    results = repo.session.execute(stmt).all()
    for row in results:
        assert row.CoinFlipResult.number_of_flips == 10
