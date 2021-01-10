from fastapi.testclient import TestClient

from src.entrypoints.api import app

client = TestClient(app)


def test_flip_coin_via_api_entrypoint():
    response = client.post("/flip/", json={"times": 10})
    assert response.status_code == 200
    resp_json = response.json()
    assert (
        resp_json["flip_results"]["heads"] + resp_json["flip_results"]["tails"]
        == resp_json["times"]
    )