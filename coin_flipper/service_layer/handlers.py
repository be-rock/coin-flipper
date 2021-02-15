from coin_flipper.domain import commands, events
from coin_flipper.domain.model import CoinFlipResult
from coin_flipper.service_layer import services


def request_coin_flip(command: commands.FlipCoin) -> CoinFlipResult:
    flip_result = services.flip_coin(command.number_of_times)
    services.persist_flip_results_to_repository(flip_results=flip_result)
    return flip_result


# def request_coin_flip_info(event: events.CoinFlipInfoRequested):
#     return services.retrieve_coin_flip_info(uuid=event.uuid)
