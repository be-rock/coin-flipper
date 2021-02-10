import random
from collections import defaultdict

from coin_flipper.domain.model import CoinFlipResult


def flip_coin(number_of_flips) -> CoinFlipResult:
    flip_results = defaultdict(int)
    for _ in range(number_of_flips):
        result = random.choice(["heads", "tails"])
        flip_results[result] += 1
    return CoinFlipResult(number_of_flips=number_of_flips, flip_results=flip_results)
