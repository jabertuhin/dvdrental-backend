from fastapi import FastAPI

from app.exceptions.handlers import add_exceptions_in_handler
from app.routes import health, actor

# TODO: Read api_version and title from config file.
api_version = 0.1
title = "DVD Rental"
app = FastAPI(title=title, version=api_version)


# including router in the app
app.include_router(health.router)
app.include_router(actor.router)


# Add exceptions
add_exceptions_in_handler(app)
