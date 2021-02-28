import datetime
import os
import uuid
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
    return CoinFlipResult(
        uuid=str(uuid.uuid4()),
        request_time=datetime.datetime.now(),
        number_of_flips=number_of_flips,
        flip_results=flip_results,
    )


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


def retrieve_coin_flip_info(
    uuid: uuid.uuid4, uow: AbstractUnitOfWork = None
) -> CoinFlipResult:
    uow = SqlAlchemyUnitOfWork() if uow is None else uow
    with uow:
        result = uow.session.execute(
            "SELECT * FROM coin_flip WHERE uuid = :uuid", dict(uuid=uuid)
        ).fetchone()
    return result
