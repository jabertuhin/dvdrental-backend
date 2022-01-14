from typing import Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.base_repository import BaseRepository
from app.db.schemas.actor import ActorSchema
from app.db.session import async_session
from app.db.tables.actor import Actor


class ActorRepository(BaseRepository):
    def __init__(
            self,
            db_session: AsyncSession = Depends(async_session),
            *args,
            **kwargs) -> None:
        super().__init__(db_session, *args, **kwargs)

    @property
    def _table(self) -> Type[Actor]:
        return Actor

    @property
    def _schema(self) -> Type[ActorSchema]:
        return ActorSchema
