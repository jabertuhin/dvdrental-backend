import inflection
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseDBModel:
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return inflection.underscore(cls.__name__)
