"""
An abstraction over the components of the repository such as a 'session' or when to 'commit' a transaction
"""

import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from coin_flipper.adapters import repository
from coin_flipper import APP_ENV, CONFIG
from coin_flipper.adapters.repository import FakeRepository

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(CONFIG["db"][APP_ENV]["uri"]),
    future=True,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

class AbstractUnitOfWork(abc.ABC):
    batches: repository.AbstractRepository

    def _enter__(self):
        """"""

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        """"""

    @abc.abstractmethod
    def rollback(self):
        """"""


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = FakeRepository()
        self.committed = False

    def __enter__(self):
        pass

    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        self.committed = True

    def rollback(self):
        """"""


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.repo = repository.SqlAlchemyRepository(self.session)
        # return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
