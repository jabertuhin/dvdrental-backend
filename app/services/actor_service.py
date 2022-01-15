from app.dtos.responses.actor import ActorsDto, ActorDto
from app.services.base_service import BaseService


class ActorService(BaseService):
    async def get_all_actors(self) -> ActorsDto:
        raise NotImplementedError()

    async def get_actor(self, actor_id: int) -> ActorDto:
        raise NotImplementedError()
