from typing import List

from pydantic import BaseModel


class ActorDto(BaseModel):
    first_name: str
    last_name: str


class ActorsDto(BaseModel):
    actors: List[ActorDto]
