from dataclasses import dataclass

class Event:
    pass

@dataclass
class CoinFlipRequested(Event):
    number_of_times: int