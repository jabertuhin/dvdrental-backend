from fastapi.applications import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.exceptions.services.actor_service_exceptions import ActorServiceException
from app.exceptions.services.base_service_exception import BaseServiceException


# Add custom exceptions in list
custom_exceptions = [ActorServiceException]


def custom_exception_handler(request: Request, exc: type[BaseServiceException]) -> JSONResponse:
    return exc.to_json_response()


def add_exceptions_in_handler(app: FastAPI) -> None:
    # add custom exceptions
    for custom_exception in custom_exceptions:
        app.add_exception_handler(custom_exception, custom_exception_handler)
