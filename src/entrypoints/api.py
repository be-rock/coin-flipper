from fastapi import FastAPI

from src.domain.api_schema import CoinFlipResult
from src.domain.model import Coin

app = FastAPI()


@app.post("/flip/", response_model=CoinFlipResult)
async def flip_coin(coinflip: CoinFlipResult):
    coin = Coin()
    result = coin.flip(number_of_flips=coinflip.number_of_flips)
    coinflip.flip_results = dict(result)
    return coinflip
