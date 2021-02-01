import random
from collections import defaultdict

# from coin_flipper.adapters.repository import SqlAlchemyRepository, on_disk_sqlite_db, sqlite_on_disk_session_factory
# from coin_flipper.domain.api_schema import CoinFlipResultApi
from coin_flipper.domain.model import CoinFlipResult


# def flip_coin(number_of_flips) -> dict:
# def flip_coin(number_of_flips) -> CoinFlipResultApi:
def flip_coin(number_of_flips) -> CoinFlipResult:
    flip_results = defaultdict(int)
    for _ in range(number_of_flips):
        result = random.choice(["heads", "tails"])
        flip_results[result] += 1
    return CoinFlipResult(number_of_flips=number_of_flips, flip_results=flip_results)


# def coin_flip_results(uuid: str):
#     repo = SqlAlchemyRepository(session_factory=sqlite_on_disk_session_factory)
#     result = repo.list(model_item=CoinFlipResult, filters={'uuid': uuid})
#     return result
