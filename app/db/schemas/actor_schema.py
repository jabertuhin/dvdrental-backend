from datetime import datetime
from typing import Optional

from app.db.schemas.base_schema import BaseSchema


class ActorSchema(BaseSchema):
    actor_id: Optional[int]
    first_name: str
    last_name: str
    last_update: Optional[datetime]
