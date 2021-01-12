from collections import defaultdict


def test_can_obtain_coinflip_results(coin_fixture):
    number_of_flips = 10
    results = coin_fixture.flip(number_of_flips=number_of_flips)
    assert isinstance(results, defaultdict)
    assert results["heads"] + results["tails"] == number_of_flips
