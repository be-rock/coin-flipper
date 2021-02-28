import json

from fastapi import APIRouter

from coin_flipper.domain import commands
from coin_flipper.domain.api_schema import CoinFlipInfoRequestedApi, CoinFlipResultApi
from coin_flipper.domain.events import CoinFlipInfoRequested
from coin_flipper.service_layer import messagebus
from coin_flipper import get_logger

logger = get_logger(logger_name=__name__)
router = APIRouter()


@router.post(
    "/flip/{number_of_flips}", response_model=CoinFlipResultApi, status_code=201
)
async def flip_coin(number_of_flips: int):
    logger.info(f"http post to '/flip/{number_of_flips}'")
    command = commands.FlipCoin(number_of_times=number_of_flips)
    result = messagebus.command_handler(command=command)
    logger.info(f"http post result: {result}'")
    return CoinFlipResultApi(
        number_of_flips=result.number_of_flips,
        flip_results=result.flip_results,
        uuid=result.uuid,
        request_time=result.request_time,
    )


@router.get("/flip/results/{uuid}", response_model=CoinFlipInfoRequestedApi)
async def flip_coin_results(uuid: str):
    logger.info(f"http get to '/flip/results/{uuid}'")
    event = CoinFlipInfoRequested(uuid=uuid)
    logger.info(f"event: {event}")
    result = messagebus.event_handler(event=event)
    _result = dict(zip(result.keys(), result))
    logger.info(f"http get result: {_result}")
    logger.info(f"flip_results: {_result['flip_results']}")
    logger.info(f"flip_results: {type(_result['flip_results'])}")
    logger.info(f"flip_results: {dir(_result['flip_results'])}")
    # logger.info(f"http get result: {result.keys()}")
    # logger.info(f"http get result: {dict(zip(result.keys(), result))}")
    # logger.info(f"http get result: {dir(result)}")
    # _result = result._as_dict()
    # logger.info(f"http get result: {_result}")
    # logger.info(f"types: {type(result)}")
    # logger.info(f"types: {type(result._as_dict())}")
    # logger.info(f"value as dict: {result._as_dict()}")
    return CoinFlipInfoRequestedApi(
        uuid=_result["uuid"],
        request_time=_result["request_time"],
        number_of_flips=_result["number_of_flips"],
        flip_results=json.loads(_result["flip_results"]),
    )
