from typing import List

from pydantic import BaseModel


class ActorDto(BaseModel):
    actor_id: int
    first_name: str
    last_name: str


class ActorsDto(BaseModel):
    actors: List[ActorDto]
