import pytest

from coin_flipper.domain.model import CoinFlipResult
from coin_flipper.service_layer.unit_of_work import FakeUnitOfWork
from coin_flipper.service_layer.unit_of_work import SqlAlchemyUnitOfWork

pytestmark = pytest.mark.usefixtures("mappers")


def test_uow_commits_transaction():
    uow = FakeUnitOfWork()
    with uow:
        uow.repo.add(["a"])
        uow.commit()
        assert uow.committed is True


def test_failed_uow_implicitly_rolls_back_transaction(
    sqlite_in_memory_session_factory, coin_flip_result_fixture
):
    uow = SqlAlchemyUnitOfWork(session_factory=sqlite_in_memory_session_factory)
    with uow:
        uow.repo.add(coin_flip_result_fixture)
        assert (
            len(uow.repo.list(model_item=CoinFlipResult)) == 1
        )  # 1 row successfully inserted
        # expect that the transaction implicitly rolls back if exception is raised
        with pytest.raises(ZeroDivisionError):
            _ = 1 / 0
    assert len(uow.repo.list(model_item=CoinFlipResult)) == 0


def test_uow_commit_persists_transaction_activity(
    sqlite_in_memory_session_factory, coin_flip_result_fixture
):
    uow = SqlAlchemyUnitOfWork(session_factory=sqlite_in_memory_session_factory)
    with uow:
        uow.repo.add(coin_flip_result_fixture)
        assert len(uow.repo.list(model_item=CoinFlipResult)) == 1
        uow.commit()
    # start new unit of work
    with uow:
        assert len(uow.repo.list(model_item=CoinFlipResult)) == 1
