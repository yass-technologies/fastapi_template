from __future__ import annotations

import logging
from contextlib import AbstractContextManager
from typing import Callable, List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from {{cookiecutter.project_name}}.core.config import settings
from {{cookiecutter.project_name}}.users.exceptions import (
    DuplicateUserError,
    UserNotFoundError,
)
from {{cookiecutter.project_name}}.users.model import User

logger = logging.getLogger(settings.logger_name)


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_external_id(self, user_external_id: str) -> User:
        with self.session_factory() as session:
            user = (
                session.query(User).filter(User.external_id == user_external_id).first()
            )
            if not user:
                raise UserNotFoundError(
                    user_external_id, UserNotFoundError.external_id_reference
                )
            return user

    def get_by_email(self, email: str) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.email == email).first()
            if not user:
                raise UserNotFoundError(email, UserNotFoundError.email_reference)
            return user

    def create(self, user: User) -> User:
        with self.session_factory() as session:
            try:
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
            except IntegrityError:
                logging.error(
                    f"Could not persist user with email {user.email}, already exist"
                )
                raise DuplicateUserError(user.email)

    def update(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            return user
