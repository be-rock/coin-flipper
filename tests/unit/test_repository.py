

def test_repository_add_items(fake_repository_fixture, coin_fixture):
    repo = fake_repository_fixture
    number_of_flips = 10
    results = coin_fixture.flip(number_of_flips=number_of_flips)
    repo.add(item=results)
    assert len(repo.items) == 1


def test_repository_delete_items(fake_repository_fixture, coin_fixture):
    repo = fake_repository_fixture
    assert len(repo.items) == 0
    repo.add(item=coin_fixture)
    assert len(repo.items) == 1
    repo.delete(coin_fixture)
    assert len(repo.items) == 0


def test_repository_list_items(fake_repository_fixture, coin_fixture):
    repo = fake_repository_fixture
    assert len(repo.items) == 0
    repo.add(item=coin_fixture)
    results = repo.list()
    assert len(results) == 1
    assert isinstance(results[0], type(coin_fixture))
