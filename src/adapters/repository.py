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


# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session_factory):
#         self.session = session_factory()
#
#     def add(self, model_item) -> None:
#         self.session.add(model_item)
#
#     def delete(self, model_item) -> None:
#         self.session.delete(model_item)
#
#     def list(self, model_item, filters: dict = None) -> list:
#         if filters:
#             stmt = select(model_item).filter_by(**filters)
#         else:
#             stmt = select(model_item)
#         return self.session.execute(stmt).all()
