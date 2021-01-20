import pytest
from sqlalchemy import select

from coin_flipper.domain.model import Coin, CoinFlipResult

pytestmark = pytest.mark.usefixtures("mappers")


def test_sqlalchemy_repository_create_coinflip_model_item(sqlalchemy_on_disk_fixture):
    repo = sqlalchemy_on_disk_fixture
    flip_num = 10
    coin = Coin()
    results = coin.flip(number_of_flips=flip_num)
    flip_model_obj = CoinFlipResult(number_of_flips=flip_num, flip_results=dict(results))
    repo.add(flip_model_obj)
    results = repo.list(model_item=CoinFlipResult, filters={'id': 1})
    assert len(results) == 1
    for row in results:
        coin_info = row[0]
        assert (
            coin_info.flip_results["heads"] + coin_info.flip_results["tails"] == flip_num
        )
    repo.delete(flip_model_obj)
    assert len(repo.list(model_item=CoinFlipResult)) == 0
