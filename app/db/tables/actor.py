from sqlalchemy import Column, Integer, TIMESTAMP, func, Sequence
from sqlalchemy.dialects.postgresql import VARCHAR

from app.db.base_class import BaseDBModel


class Actor(BaseDBModel):
    actor_id = Column(Integer, Sequence('actor_actor_id_seq'),
                      primary_key=True, nullable=False, unique=True, autoincrement=True)
    first_name = Column(VARCHAR(45), nullable=False)
    last_name = Column(VARCHAR(45), nullable=False)
    last_update = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
