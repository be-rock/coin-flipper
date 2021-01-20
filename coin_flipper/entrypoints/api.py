from fastapi import FastAPI

from coin_flipper.domain.api_schema import CoinFlipResult
from coin_flipper.domain.model import Coin

app = FastAPI()


@app.post("/flip/", response_model=CoinFlipResult)
async def flip_coin(coin_flip_api: CoinFlipResult):
    coin = Coin()
    result = coin.flip(number_of_flips=coin_flip_api.number_of_flips)
    coin_flip_api.flip_results = dict(result)
    return coin_flip_api
