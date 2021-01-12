import pytest
from sqlalchemy import select

from src.domain.model import Coin, CoinFlipResult

pytestmark = pytest.mark.usefixtures("mappers")


# @pytest.mark.skip
def test_sqlalchemy_repository_create_coinflip_model_item(
    sqlalchemy_on_disk_fixture
):
    repo = sqlalchemy_on_disk_fixture
    flip_num = 10
    coin = Coin()
    results = coin.flip(number_of_flips=flip_num)
    # print(results)
    flip_model_obj = CoinFlipResult(number_of_flips=flip_num, flip_results=dict(results))
    print(flip_model_obj)
    # repo.add(flip_model_obj)

    # repo.session.commit()
    # stmt = select(CoinFlip)
    # results = repo.session.execute(stmt).all()
    # assert "bob" in [row.Customer.fname for row in results]
