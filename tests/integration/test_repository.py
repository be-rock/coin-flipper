import pytest
from sqlalchemy import select

from src.domain.model import CoinFlipResult

pytestmark = pytest.mark.usefixtures("mappers")

@pytest.mark.skip
def test_sqlalchemy_repository_create_coinflip_model_item(
    sqlalchemy_in_memory_fixture, coin_flip_fixture
):
    repo = sqlalchemy_in_memory_fixture
    repo.add(coin_flip_fixture)
    # stmt = select(CoinFlip)
    # results = repo.session.execute(stmt).all()
    # assert "bob" in [row.Customer.fname for row in results]
