
def test_can_define_number_of_coin_flips(test_coin_fixture):
    assert test_coin_fixture.number_of_flips == 10


def test_can_flip_coin(test_coin_fixture):
    res = test_coin_fixture.flip()
    assert res["heads"] + res["tails"] == test_coin_fixture.number_of_flips