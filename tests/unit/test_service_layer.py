from src.service_layer import messagebus
from src.domain import events

def test_messagebus_flip_request_received():
    event = events.CoinFlipRequested(number_of_flips=10)
    print(event)
    print(type(event))
    res = messagebus.handle(event=event)
    print(res)

