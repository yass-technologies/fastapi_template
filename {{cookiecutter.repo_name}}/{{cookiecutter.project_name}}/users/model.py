from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import String
from sqlmodel import Field, SQLModel

# from fanatiques_api.misc.sql_database.database import Base


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: Optional[str] = Field(sa_column=Column(String, unique=True))
    email: EmailStr = Field(
        index=True, sa_column=Column("email", String, unique=True, nullable=False)
    )
    password: str
    is_active: bool = True
    is_verified: bool = False
    created_at: datetime = Field(default=datetime.utcnow())
    first_name: str
    last_name: str

    __tablename__: str = "users"  # type: ignore
