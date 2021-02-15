from fastapi import FastAPI
from sqlalchemy import create_engine

from coin_flipper import APP_ENV, CONFIG
from coin_flipper.entrypoints.api.routes import router as api_router
from coin_flipper.adapters.orm import metadata, start_mappers

SUPPORTED_API_VERSION = 1
API_PREFIX = "/api"
app = FastAPI()

# todo - entrypoint tightly-coupled to orm
metadata.create_all(create_engine(CONFIG["db"][APP_ENV]["uri"]))
start_mappers()


for supported_api_version in range(1, SUPPORTED_API_VERSION + 1):
    app.include_router(
        api_router,
        prefix=f"{API_PREFIX}/v{supported_api_version}",
        tags=[f"v{supported_api_version}"],
    )
