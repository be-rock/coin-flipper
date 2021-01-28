"""
the domain model as represented by the api
"""
import datetime
import uuid
from collections import defaultdict

from pydantic import BaseModel


class CoinFlipResultApi(BaseModel):
    request_time: datetime.datetime = datetime.datetime.now()
    uuid: str = uuid.uuid4()
    number_of_flips: int
    flip_results: defaultdict = defaultdict(int)
