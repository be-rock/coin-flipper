from src.adapters.repository import FakeRepository


def test_repository_add_items(fake_repository_fixture):
    repo = fake_repository_fixture
    repo.add(item={"asdf": "qwer"})
    assert len(repo.items) == 1
    assert "asdf" in repo.items[0]


def test_repository_delete_items(fake_repository_fixture):
    repo = fake_repository_fixture
    assert len(repo.items) == 0
    repo.add(item={'asdf': 'qwer'})
    assert len(repo.items) == 1
    repo.delete({'asdf': 'qwer'})
    assert len(repo.items) == 0
