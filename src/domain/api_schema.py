"""
the domain model as represented by the api
TODO - look at pydantic usage of dataclass. ref:
    https://pydantic-docs.helpmanual.io/usage/dataclasses/
"""
import datetime
import uuid
from collections import defaultdict

from pydantic import BaseModel


class CoinFlipBase(BaseModel):
    """"""

    request_time: datetime.datetime = datetime.datetime.now()


class CoinFlipResult(CoinFlipBase):
    number_of_flips: int
    uuid: str = str(uuid.uuid4())
    flip_results: defaultdict = defaultdict(int)
