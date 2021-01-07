import random


class Coin:
    def __init__(self, number_of_flips: int):
        self.number_of_flips = number_of_flips
        self._flip_allocations = {'heads': 0, 'tails': 0}

    def flip(self) -> dict:
        for _ in range(self.number_of_flips):
            result = random.choice(list(self._flip_allocations))
            self._flip_allocations[result] += 1
        return self._flip_allocations


