from app.exceptions.services.base_service_exception import BaseServiceException


class ActorServiceException(BaseServiceException):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(status_code=status_code, message=message)
