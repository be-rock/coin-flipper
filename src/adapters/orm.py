"""
mapping between the domain model and the database model
"""
import datetime
from collections import defaultdict
from dataclasses import dataclass

from sqlalchemy import Column, DateTime, Integer, JSON, String, Table
from sqlalchemy.orm import registry

from src.domain import model

mapper_registry = registry()
metadata = mapper_registry.metadata

coin_flip = Table(
    "coin_flip",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("uuid", String),
    Column("number_of_flips", Integer),
    Column("request_time", DateTime),
    Column("flip_results", JSON),
)

import uuid
@dataclass
class CoinFlipResult():
    """"""
    number_of_flips: int
    uuid: str = str(uuid.uuid4())
    flip_results: defaultdict = lambda: defaultdict(int)
    request_time: datetime.datetime = datetime.datetime.now()



def start_mappers() -> None:
    # mapper_registry.map_imperatively(model.CoinFlipResult, coin_flip)
    mapper_registry.map_imperatively(CoinFlipResult, coin_flip)
