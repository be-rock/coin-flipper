import random
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Coin:
    number_of_flips: int = 0
    _flip_allocations: defaultdict = field(
        init=False, repr=True, default_factory=lambda: defaultdict(int)
    )

    def flip(self) -> dict:
        for _ in range(self.number_of_flips):
            result = random.choice(['heads', 'tails'])
            self._flip_allocations[result] += 1
        return self._flip_allocations
