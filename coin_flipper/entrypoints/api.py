import datetime
import uuid

from fastapi import FastAPI

from coin_flipper.domain.api_schema import CoinFlipResult
from coin_flipper.domain.events import CoinFlipRequested
from coin_flipper.service_layer import messagebus

app = FastAPI()


# @app.post("/flip/", response_model=CoinFlipResult)
# async def flip_coin(coin_flip_api: CoinFlipResult):
#     event = CoinFlipRequested(number_of_times=coin_flip_api.number_of_flips)
#     result = messagebus.handle(event=event)
#     coin_flip_api.flip_results = dict(result)
#     return coin_flip_api


@app.post("/flip/{number_of_flips}", response_model=CoinFlipResult)
async def flip_coin(number_of_flips: int):
    event = CoinFlipRequested(number_of_times=number_of_flips)
    result = messagebus.handle(event=event)
    return CoinFlipResult(
        number_of_flips=number_of_flips,
        flip_results=result,
        uuid=str(uuid.uuid4()),
        request_time=datetime.datetime.now(),
    )
