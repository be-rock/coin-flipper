from typing import Callable

from coin_flipper.domain import events
from coin_flipper.service_layer import services


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        return handler(event)


def request_coin_flip(event: events.CoinFlipRequested):
    return services.flip_coin(event.number_of_times)


HANDLERS: dict[events, list[Callable]] = {
    events.CoinFlipRequested: [request_coin_flip],
}
