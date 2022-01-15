from unittest.mock import AsyncMock

import pytest

from app.db.repositories.actor_repository import ActorRepository
from app.dtos.responses.actor import ActorDto, ActorsDto
from app.exceptions.services.actor_service_exceptions import ActorServiceException
from app.services.implementations.actor_service_implementation import ActorServiceImplementation


@pytest.fixture
def mock_repository() -> AsyncMock:
    mock_repository = AsyncMock(wraps=ActorRepository)
    return mock_repository


@pytest.mark.asyncio
async def test_get_all_actors_when_actors_are_available_should_return_ActorsDto(mock_repository):
    actors = [
        ActorDto(first_name="A", last_name="B"),
        ActorDto(first_name="C", last_name="D"),
        ActorDto(first_name="E", last_name="F"),
    ]
    mock_repository.get_all.return_value = actors
    actor_service = ActorServiceImplementation(mock_repository)

    actual = await actor_service.get_all_actors()

    assert isinstance(actual, ActorsDto)
    assert actual.actors == actors
    mock_repository.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_actor_when_actor_id_is_valid_should_return_ActorDto(mock_repository):
    actor = ActorDto(first_name="A", last_name="B")
    mock_repository.get_by_id.return_value = actor
    actor_service = ActorServiceImplementation(mock_repository)

    actual = await actor_service.get_actor(actor_id=20)

    assert isinstance(actual, ActorDto)
    assert actual == actor
    mock_repository.get_by_id.assert_called_once()


@pytest.mark.asyncio
async def test_get_actor_when_actor_id_is_unavailable_should_return_ActorServiceException(mock_repository):
    mock_repository.get_by_id.return_value = None
    actor_service = ActorServiceImplementation(mock_repository)

    with pytest.raises(ActorServiceException) as excinfo:
        _ = await actor_service.get_actor(actor_id=650)

    assert excinfo.value.status_code == 404
    assert excinfo.value.message == "650 actor id is not available."

