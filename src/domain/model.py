import random
from collections import defaultdict
import datetime
import uuid

from pydantic import BaseModel


class Coin:
    def __init__(self, number_of_flips: int = 0):
        self.number_of_flips = number_of_flips
        self._flip_allocations: defaultdict = defaultdict(int)

    def flip(self) -> dict:
        for _ in range(self.number_of_flips):
            result = random.choice(["heads", "tails"])
            self._flip_allocations[result] += 1
        return self._flip_allocations


class CoinFlip(BaseModel):
    uuid: str = str(uuid.uuid4())
    times: int
    request_time: datetime.datetime = datetime.datetime.now()
    flip_results: defaultdict = defaultdict(int)
