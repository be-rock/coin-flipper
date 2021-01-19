from fastapi import FastAPI

from coin_flipper.domain.api_schema import CoinFlipResult
from coin_flipper.domain.model import Coin

app = FastAPI()


@app.post("/flip/", response_model=CoinFlipResult)
async def flip_coin(coinflip: CoinFlipResult):
    coin = Coin()
    result = coin.flip(number_of_flips=coinflip.number_of_flips)
    coinflip.flip_results = dict(result)
    return coinflip
