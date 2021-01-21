import random
from collections import defaultdict

from coin_flipper.adapters.repository import SqlAlchemyRepository, on_disk_sqlite_db, sqlite_on_disk_session_factory
from coin_flipper.domain.model import CoinFlipResult


def flip_coin(number_of_flips) -> dict:
    flip_results = defaultdict(int)
    for _ in range(number_of_flips):
        result = random.choice(["heads", "tails"])
        flip_results[result] += 1
    return flip_results


# def coin_flip_results(uuid: str):
#     repo = SqlAlchemyRepository(session_factory=sqlite_on_disk_session_factory)
#     result = repo.list(model_item=CoinFlipResult, filters={'uuid': uuid})
#     return result
