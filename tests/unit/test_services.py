import pytest

from coin_flipper.domain.events import CoinFlipInfoRequested, CoinFlipRequested
from coin_flipper.domain.model import Coin, CoinFlipResult
from coin_flipper.service_layer import messagebus

pytestmark = pytest.mark.usefixtures("mappers")

def test_coin_flip_event():
    number_of_flips_from_the_api = 10
    event = CoinFlipRequested(number_of_times=number_of_flips_from_the_api)
    result = messagebus.handle(event=event)
    assert result["heads"] + result["tails"] == number_of_flips_from_the_api


def test_coin_flip_results(sqlalchemy_in_memory_fixture):
    repo = sqlalchemy_in_memory_fixture
    flip_num = 10
    coin = Coin()
    results = coin.flip(number_of_flips=flip_num)
    flip_model_obj = CoinFlipResult(
        number_of_flips=flip_num, flip_results=dict(results)
    )
    repo.add(flip_model_obj)
    results = repo.list(model_item=CoinFlipResult, filters={'uuid': flip_model_obj.uuid})
    # event = CoinFlipInfoRequested(uuid=flip_model_obj.uuid)
    # result = messagebus.handle(event=event)
    # first row, first column
    assert results[0][0].uuid == flip_model_obj.uuid
    # todo - need to abstract away the service to not have a hard dependency on the repository
    # repo = SqlAlchemyRepository(session_factory=on_disk_sqlite_db())
    # result = repo.list(model_item=CoinFlipResult, filters={'uuid': uuid})
    # return
