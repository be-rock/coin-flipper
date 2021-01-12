import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from src.adapters.orm import metadata, start_mappers
from src.adapters.repository import FakeRepository, SqlAlchemyRepository
from src.domain.model import Coin, CoinFlipResult


@pytest.fixture()
def coin_fixture():
    yield Coin()


# @pytest.fixture()
# def coin_flip_fixture():
#     yield CoinFlipResult(number_of_flips=10)


@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine("sqlite:///:memory:", future=True)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_in_memory_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db, future=True)


@pytest.fixture()
def sqlalchemy_in_memory_fixture(sqlite_in_memory_session_factory):
    yield SqlAlchemyRepository(session_factory=sqlite_in_memory_session_factory)


@pytest.fixture
def on_disk_sqlite_db():
    engine = create_engine("sqlite:////tmp/test.db", future=True)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_on_disk_session_factory(on_disk_sqlite_db):
    yield sessionmaker(bind=on_disk_sqlite_db, future=True)


@pytest.fixture()
def sqlalchemy_on_disk_fixture(sqlite_on_disk_session_factory):
    yield SqlAlchemyRepository(session_factory=sqlite_on_disk_session_factory)


@pytest.fixture()
def fake_repository_fixture():
    yield FakeRepository()


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()
