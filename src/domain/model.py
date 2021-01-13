import random
from collections import defaultdict
import datetime
import uuid
from dataclasses import dataclass

from pydantic import BaseModel


class Coin:
    # def __init__(self, number_of_flips: int = 0):
    def __init__(self):
        # self.number_of_flips = number_of_flips
        # self.coin_type = coin_type
        self.flip_results: defaultdict = defaultdict(int)

    def flip(self, number_of_flips) -> dict:
        for _ in range(number_of_flips):
            result = random.choice(["heads", "tails"])
            self.flip_results[result] += 1
        return self.flip_results


@dataclass
class CoinFlipResult:
    number_of_flips: int
    flip_results: dict
    request_time: datetime.datetime = datetime.datetime.now()
    uuid: str = str(uuid.uuid4())
