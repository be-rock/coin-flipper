from typing import Callable

from coin_flipper.domain import commands, events
from coin_flipper.service_layer import services


# def handle(event: events.Event):
#     for handler in HANDLERS[type(event)]:
#         return handler(event)

def command_handler(command: commands.Command):
    for handler in HANDLERS[type(command)]:
        return handler(command)


def request_coin_flip(command: commands.FlipCoin):
    return services.flip_coin(command.number_of_times)


# def request_coin_flip_results(event: events.CoinFlipInfoRequested):
#     return services.coin_flip_results(event.uuid)


HANDLERS: dict[events, list[Callable]] = {
    commands.FlipCoin: [request_coin_flip],
    # events.CoinFlipInfoRequested: [request_coin_flip_results],
}
