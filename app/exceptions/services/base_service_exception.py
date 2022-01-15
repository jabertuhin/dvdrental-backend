from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class BaseServiceException(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message

    def to_json_response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code,
            content=jsonable_encoder({"message": self.message})
        )
