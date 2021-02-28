from coin_flipper.domain import commands, events
from coin_flipper.service_layer import handlers


def event_handler(event: events.Event):
    for handler in EVENT_HANDLERS[type(event)]:
        return handler(event)


def command_handler(command: commands.Command):
    for handler in COMMAND_HANDLERS[type(command)]:
        return handler(command)


COMMAND_HANDLERS = {
    commands.FlipCoin: [handlers.request_coin_flip],
}
EVENT_HANDLERS = {events.CoinFlipInfoRequested: [handlers.request_coin_flip_info]}
