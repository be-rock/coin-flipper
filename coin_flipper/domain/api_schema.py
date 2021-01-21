"""
the domain model as represented by the api
"""
import datetime
from collections import defaultdict

from pydantic import BaseModel


class CoinFlipResult(BaseModel):
    request_time: datetime.datetime
    uuid: str
    number_of_flips: int
    flip_results: defaultdict = defaultdict(int)
