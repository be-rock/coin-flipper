import datetime
import random
import uuid
from collections import defaultdict
from dataclasses import dataclass

from coin_flipper.domain import events


class Coin:
    def __init__(self):
        self.flip_results: defaultdict = defaultdict(int)
        self.events_: list[events.Event] = []

    def flip(self, number_of_flips) -> dict:
        for _ in range(number_of_flips):
            result = random.choice(["heads", "tails"])
            self.flip_results[result] += 1
        return self.flip_results


@dataclass
class CoinFlipResult:
    number_of_flips: int
    flip_results: dict
    request_time: datetime.datetime
    uuid: str
