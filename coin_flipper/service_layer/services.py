import os
import random
from collections import defaultdict

from coin_flipper.domain.model import CoinFlipResult
from coin_flipper.service_layer.unit_of_work import (
    AbstractUnitOfWork,
    FakeUnitOfWork,
    SqlAlchemyUnitOfWork,
)


def flip_coin(number_of_flips) -> CoinFlipResult:
    flip_results = defaultdict(int)
    for _ in range(number_of_flips):
        result = random.choice(["heads", "tails"])
        flip_results[result] += 1
    return CoinFlipResult(number_of_flips=number_of_flips, flip_results=flip_results)


def persist_flip_results_to_repository(
    flip_results: CoinFlipResult, uow: AbstractUnitOfWork = None,
):
    if uow is None:
        uow = (
            FakeUnitOfWork()
            if os.getenv("APP_ENV") != "prod"
            else SqlAlchemyUnitOfWork()
        )
    with uow:
        uow.repo.add(flip_results)
        uow.commit()


# def retrieve_coin_flip_info(
#     uuid: uuid.uuid4, uow: AbstractUnitOfWork = None
# ) -> list[CoinFlipResult]:
#     if not uow:
#         uow = SqlAlchemyUnitOfWork()
#     result = uow.repo.list(model_item=CoinFlipResult, filters={"uuid": uuid})
#     return result
