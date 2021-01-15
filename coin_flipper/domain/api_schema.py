"""
the domain model as represented by the api
"""
import datetime
import uuid
from collections import defaultdict

from pydantic import BaseModel


class ApiBaseModel(BaseModel):
    request_time: datetime.datetime = datetime.datetime.now()


class CoinFlipResult(ApiBaseModel):
    number_of_flips: int
    uuid: str = str(uuid.uuid4())
    flip_results: defaultdict = defaultdict(int)
