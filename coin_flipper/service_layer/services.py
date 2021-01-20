import random
from collections import defaultdict


def flip_coin(number_of_flips) -> dict:
    flip_results = defaultdict(int)
    for _ in range(number_of_flips):
        result = random.choice(["heads", "tails"])
        flip_results[result] += 1
    return flip_results
