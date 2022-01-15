from fastapi import Depends, status

from app.db.repositories.actor_repository import ActorRepository
from app.db.repositories.base_repository import BaseRepository
from app.dtos.responses.actor import ActorsDto, ActorDto
from app.exceptions.exception_messages.actor_service import ACTOR_ID_NOT_AVAILABLE_EXCEPTION_MESSAGE
from app.exceptions.services.actor_service_exceptions import ActorServiceException
from app.services.actor_service import ActorService


class ActorServiceImplementation(ActorService):
    def __init__(
            self,
            actor_repository: BaseRepository = Depends(ActorRepository)
    ):
        self._actor_repository = actor_repository

    async def get_all_actors(self) -> ActorsDto:
        actors = await self._actor_repository.get_all()
        return ActorsDto(actors=actors)

    async def get_actor(self, actor_id: int) -> ActorDto:
        actor = await self._actor_repository.get_by_id(actor_id)
        if actor:
            return actor
        raise ActorServiceException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=ACTOR_ID_NOT_AVAILABLE_EXCEPTION_MESSAGE.format(actor_id)
        )
