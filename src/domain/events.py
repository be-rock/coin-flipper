import datetime
from dataclasses import dataclass


@dataclass
class Event:
    """"""


@dataclass
class CoinFlipRequested(Event):
    """"""

    number_of_flips: int
    event_datetime: datetime = datetime.datetime.now()
