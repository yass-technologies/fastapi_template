from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from {{cookiecutter.project_name}}.users.model import User


class UserCreationIntention(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

    def __init__(
        self, email: str, password: str, first_name: str, last_name: str
    ) -> None:
        super().__init__(
            email=email, password=password, first_name=first_name, last_name=last_name
        )

    def to_model(self) -> User:
        return User(
            external_id=None,
            email=EmailStr(self.email),
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )


class UserCredentials(BaseModel):
    email: str
    password: str

    def __init__(self, email: str, password: str) -> None:
        super().__init__(email=email, password=password)


class UserDTO(BaseModel):
    id: int
    external_id: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False
    created_at: datetime
    first_name: str
    last_name: str
