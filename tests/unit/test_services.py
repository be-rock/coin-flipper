from coin_flipper.domain.events import CoinFlipRequested
from coin_flipper.service_layer import messagebus


def test_coin_flip_event():
    number_of_flips_from_the_api = 10
    event = CoinFlipRequested(number_of_times=number_of_flips_from_the_api)
    result = messagebus.handle(event=event)
    assert result["heads"] + result["tails"] == number_of_flips_from_the_api
