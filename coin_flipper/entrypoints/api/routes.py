from fastapi import APIRouter

from coin_flipper.domain.api_schema import CoinFlipResultApi
from coin_flipper.domain.events import CoinFlipRequested, CoinFlipInfoRequested
from coin_flipper.service_layer import messagebus

router = APIRouter()


@router.post("/flip/{number_of_flips}", response_model=CoinFlipResultApi)
async def flip_coin(number_of_flips: int):
    event = CoinFlipRequested(number_of_times=number_of_flips)
    result = messagebus.handle(event=event)
    return CoinFlipResultApi(
        number_of_flips=result.number_of_flips,
        flip_results=result.flip_results,
        uuid=result.uuid,
        request_time=result.request_time,
    )


# @router.get("/flip/results/{uuid}", response_model=CoinFlipInfoRequested)
# async def flip_coin_results(uuid: str):
#     event = CoinFlipInfoRequested(uuid=uuid)
#     result = messagebus.handle(event=event)
#     return {'a': 'b'}
