import pytest
from fastapi.testclient import TestClient

from coin_flipper.domain.events import CoinFlipInfoRequested
from coin_flipper.entrypoints.api.routes import router
from coin_flipper.entrypoints.api.app import app, API_PREFIX
from coin_flipper.service_layer import messagebus
from coin_flipper.service_layer.unit_of_work import SqlAlchemyUnitOfWork

app.include_router(router, prefix=API_PREFIX)
client = TestClient(app)

pytestmark = pytest.mark.usefixtures("mappers")


def test_flip_coin_via_api_entrypoint():
    number_of_flips = 10
    response = client.post(f"{API_PREFIX}/flip/{number_of_flips}")
    assert response.status_code == 201
    resp_json = response.json()
    assert (
        resp_json["flip_results"]["heads"] + resp_json["flip_results"]["tails"]
        == resp_json["number_of_flips"]
    )


def test_get_coin_flip_results(coin_flip_result_fixture):
    uow = SqlAlchemyUnitOfWork()
    with uow:
        uow.repo.add(coin_flip_result_fixture)
        uow.commit()
    response = client.get(f"{API_PREFIX}/flip/results/{coin_flip_result_fixture.uuid}")
    print(response)
    # event = CoinFlipInfoRequested(uuid=coin_flip_result_fixture.uuid)
    # result = messagebus.event_handler(event=event)

    # assert response.uuid == coin_flip_result_fixture.uuid
    # cleanup
    with uow:
        uow.repo.delete(model_item=coin_flip_result_fixture)
        uow.commit()
    # async def flip_coin_results(uuid: str):
    #     event = CoinFlipInfoRequested(uuid=uuid)
    #     result = messagebus.handle(event=event)
    #     return {'a': 'b'}
