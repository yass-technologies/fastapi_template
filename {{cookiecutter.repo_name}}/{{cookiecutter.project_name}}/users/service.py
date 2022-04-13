from typing import List
from uuid import uuid4

from .model import User
from .repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_all(self) -> List[User]:
        return self._repository.get_all()

    def get_by_external_id(self, user_external_id: str) -> User:
        return self._repository.get_by_external_id(user_external_id)

    def get_by_email(self, email: str) -> User:
        return self._repository.get_by_email(email)

    def create(self, user: User) -> User:
        # FixMe: We need a encoder
        user.password = user.password
        user.external_id = str(uuid4())
        return self._repository.create(user)

    def update(self, user: User) -> User:
        return self._repository.update(user)
