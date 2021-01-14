"""
mapping between the domain model and the database model
"""

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


def start_mappers() -> None:
    mapper_registry.map_imperatively(model.CoinFlipResult, coin_flip)
