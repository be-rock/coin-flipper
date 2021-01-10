import random
from collections import defaultdict
import datetime
import uuid

from pydantic import BaseModel


class Coin:
    def __init__(self, number_of_flips: int = 0):
        self.number_of_flips = number_of_flips
        self.flip_results: defaultdict = defaultdict(int)

    def flip(self) -> dict:
        for _ in range(self.number_of_flips):
            result = random.choice(["heads", "tails"])
            self.flip_results[result] += 1
        return self.flip_results


class CoinFlip(BaseModel):
    uuid: str = str(uuid.uuid4())
    number_of_flips: int
    request_time: datetime.datetime = datetime.datetime.now()
    flip_results: defaultdict = defaultdict(int)
