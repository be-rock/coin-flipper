import pytest

from coin_flipper.domain.model import Coin, CoinFlipResult
from coin_flipper.service_layer.unit_of_work import SqlAlchemyUnitOfWork

pytestmark = pytest.mark.usefixtures("mappers")


def test_sqlalchemy_session_is_valid(sqlite_on_disk_session_factory):
    uow = SqlAlchemyUnitOfWork(session_factory=sqlite_on_disk_session_factory)
    with uow:
        assert uow.session.is_active


def test_sqlalchemy_repository_create_and_persist_coinflip_model_item(
    sqlite_on_disk_session_factory,
):
    flip_num = 10
    coin = Coin()
    results = coin.flip(number_of_flips=flip_num)
    flip_model_obj = CoinFlipResult(
        number_of_flips=flip_num, flip_results=dict(results)
    )
    uow = SqlAlchemyUnitOfWork(session_factory=sqlite_on_disk_session_factory)
    with uow:
        uow.repo.add(flip_model_obj)
        uow.commit()
        assert len(uow.repo.list(model_item=CoinFlipResult)) == 1
        assert (
            len(uow.repo.list(model_item=CoinFlipResult, filters={"id": 1})) == 1
        )  # with filter

    # model still exists in a new uow
    with uow:
        assert len(uow.repo.list(model_item=CoinFlipResult)) == 1
        uow.repo.delete(model_item=flip_model_obj)
        uow.commit()
        assert len(uow.repo.list(model_item=CoinFlipResult)) == 0
