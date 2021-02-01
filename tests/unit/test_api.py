from fastapi.testclient import TestClient

from coin_flipper.entrypoints.api.routes import router
from coin_flipper.entrypoints.api.app import app, API_PREFIX


app.include_router(router, prefix=API_PREFIX)
client = TestClient(app)


def test_flip_coin_via_api_entrypoint():
    number_of_flips = 10
    response = client.post(f"{API_PREFIX}/flip/{number_of_flips}")
    assert response.status_code == 200
    resp_json = response.json()
    assert (
        resp_json["flip_results"]["heads"] + resp_json["flip_results"]["tails"]
        == resp_json["number_of_flips"]
    )
