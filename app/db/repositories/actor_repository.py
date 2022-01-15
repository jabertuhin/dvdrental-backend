from typing import Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.base_repository import BaseRepository
from app.db.schemas.actor_schema import ActorSchema
from app.db.tables.actor import Actor
from app.db.utils import get_db_session


class ActorRepository(BaseRepository):
    def __init__(
            self,
            db_session: AsyncSession = Depends(get_db_session)
    ) -> None:
        super().__init__(db_session)

    @property
    def _table(self) -> Type[Actor]:
        return Actor

    @property
    def _schema(self) -> Type[ActorSchema]:
        return ActorSchema
