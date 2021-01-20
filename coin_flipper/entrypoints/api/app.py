from fastapi import FastAPI

from coin_flipper.entrypoints.api.routes import router as api_router

SUPPORTED_API_VERSION = 1
API_PREFIX = "/api"

app = FastAPI()

for supported_api_version in range(1, SUPPORTED_API_VERSION + 1):
    app.include_router(
        api_router,
        prefix=f"{API_PREFIX}/v{supported_api_version}",
        tags=[f"v{supported_api_version}"],
    )
