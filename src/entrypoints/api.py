from fastapi import FastAPI

from src.domain.model import Coin
from src.domain.model import CoinFlip


app = FastAPI()


@app.post("/flip/", response_model=CoinFlip)
async def flip_coin(coinflip: CoinFlip):
    coin = Coin(coinflip.times)
    result = coin.flip()
    coinflip.flip_results = dict(result)
    return coinflip
