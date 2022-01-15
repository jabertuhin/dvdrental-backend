from datetime import datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.actor_repository import ActorRepository
from app.db.schemas.actor_schema import ActorSchema
from app.db.session import async_session


# This test file was created to test Database Connection.


"""
@pytest.fixture
async def db_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@pytest.mark.asyncio
async def test_get_by_id(db_session):
    actor_repository = ActorRepository(db_session)

    expected = ActorSchema(
        actor_id=199,
        first_name="Julia",
        last_name="Fawcett",
        last_update=datetime(year=2013, month=5, day=26)
    )

    actual = await actor_repository.get_by_id(199)

    assert actual.actor_id == expected.actor_id
    assert actual.first_name == expected.first_name
    assert actual.last_name == expected.last_name


@pytest.mark.asyncio
async def test_get_by_id_when_id_not_available(db_session):
    actor_repository = ActorRepository(db_session)

    actual = await actor_repository.get_by_id(205)

    assert actual is None


@pytest.mark.asyncio
async def test_get_all(db_session):
    actor_repository = ActorRepository(db_session)

    expected = 201

    actual = await actor_repository.get_all()

    assert len(actual) == expected


@pytest.mark.asyncio
async def test_create(db_session):
    actor_repository = ActorRepository(db_session)

    actor = ActorSchema(first_name="Shahrukh", last_name="Khan")

    _ = await actor_repository.create(actor)

    actual = (await db_session.execute("SELECT COUNT(*) FROM actor;")).scalar()

    assert actual == 201
"""
