from fastapi.testclient import TestClient

from coin_flipper.entrypoints.api import app

client = TestClient(app)


def test_flip_coin_via_api_entrypoint():
    response = client.post("/flip/", json={"number_of_flips": 10})
    assert response.status_code == 200
    resp_json = response.json()
    assert (
        resp_json["flip_results"]["heads"] + resp_json["flip_results"]["tails"]
        == resp_json["number_of_flips"]
    )
