from abc import ABC, abstractmethod

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from coin_flipper.adapters.orm import metadata


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, **kwargs):
        """"""

    @abstractmethod
    def delete(self, **kwargs):
        """"""

    @abstractmethod
    def list(self, **kwargs):
        """"""


class FakeRepository(AbstractRepository):
    def __init__(self, items=None):
        self.items = items or []

    def add(self, item) -> None:
        self.items.append(item)

    def delete(self, item: list) -> None:
        self.items.remove(item)

    def list(self) -> list:
        return self.items


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session_factory):
        self.session = session_factory()

    def add(self, model_item) -> None:
        self.session.add(model_item)

    def delete(self, model_item) -> None:
        self.session.delete(model_item)

    def list(self, model_item, filters: dict = None) -> list:
        """
        : model_item: sqlalchemy mapped orm model
        : filters: keyword arguments that match to column keys or ORM attribute names
              example:
                  select(User).filter_by(name='spongebob', fullname='Spongebob Squarepants')
                  equates to:
                  ...
                  WHERE user_account.name = :name_1 AND user_account.fullname = :fullname_1
                  ...
        """
        if filters:
            stmt = select(model_item).filter_by(**filters)
        else:
            stmt = select(model_item)
        return self.session.execute(stmt).all()


# def on_disk_sqlite_db():
#     engine = create_engine("sqlite:////tmp/test.db", future=True)
#     metadata.create_all(engine)
#     return engine


# def sqlite_on_disk_session_factory(db=on_disk_sqlite_db):
#     yield sessionmaker(bind=db, future=True)
