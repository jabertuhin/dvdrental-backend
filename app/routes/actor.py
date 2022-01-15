from fastapi import APIRouter, Depends

from app.dtos.responses.actor import ActorsDto, ActorDto
from app.services.actor_service import ActorService
from app.services.implementations.actor_service_implementation import ActorServiceImplementation

router = APIRouter(tags=["Actor Resource"])


@router.get(path="/actors", response_model=ActorsDto)
async def get_actors(actor_service: ActorService = Depends(ActorServiceImplementation)) -> ActorsDto:
    return await actor_service.get_all_actors()


@router.get(path="/actors/{actor_id}", response_model=ActorDto)
async def get_actor(actor_id: int, actor_service: ActorService = Depends(ActorServiceImplementation)) -> ActorDto:
    return await actor_service.get_actor(actor_id=actor_id)
