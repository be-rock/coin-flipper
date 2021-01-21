#!/usr/bin/env bash

APP_HOST='localhost'
APP_PORT='8000'

uvicorn coin_flipper.entrypoints.api.app:app --host $APP_HOST --port $APP_PORT
