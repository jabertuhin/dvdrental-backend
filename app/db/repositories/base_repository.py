import abc
from abc import ABC
from typing import Type, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.base_db_model import BaseDBModel
from app.db.schemas.base_schema import BaseSchema


class BaseRepository(ABC):
    def __init__(self, db_session: AsyncSession, *args, **kwargs) -> None:
        self._db_session = db_session

    @property
    @abc.abstractmethod
    def _table(self) -> Type[BaseDBModel]:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def _schema(self) -> Type[BaseSchema]:
        raise NotImplementedError()

    async def get_all(self) -> List[Type[BaseSchema]]:
        query = select(self._table)
        entries = (await self._db_session.execute(query)).scalars()

        return [self._schema.from_orm(entry) for entry in entries]

    async def get_by_id(self, entity_id: int) -> Type[BaseSchema]:
        entity = await self._db_session.get(self._table, entity_id)
        return self._schema.from_orm(entity)

    async def create(self, entry: Type[BaseSchema]) -> None:
        entity = self._table(**entry.dict(exclude_none=True))
        self._db_session.add(entity)
        await self._db_session.commit()
