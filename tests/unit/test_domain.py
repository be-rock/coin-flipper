def test_can_define_number_of_coin_flips(coin_fixture):
    assert coin_fixture.number_of_flips == 10


def test_can_flip_coin(coin_fixture):
    result = coin_fixture.flip()
    assert result["heads"] + result["tails"] == coin_fixture.number_of_flips
