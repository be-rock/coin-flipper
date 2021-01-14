from src.domain import events, model


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


def flip_coin(event: events.CoinFlipRequested) -> dict:
    coin = model.Coin()
    print('in flip_coin', coin, event.number_of_flips)
    return coin.flip(number_of_flips=event.number_of_flips)


HANDLERS = {
    events.CoinFlipRequested: [flip_coin],
}
