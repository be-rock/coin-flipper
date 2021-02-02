from abc import ABC, abstractmethod

from sqlalchemy import select


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
    def __init__(self, session):
        self.session = session

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
        ref: https://docs.sqlalchemy.org/en/latest/orm/queryguide.html
        """
        if filters:
            stmt = select(model_item).filter_by(**filters)
        else:
            stmt = select(model_item)
        return self.session.execute(stmt).all()
