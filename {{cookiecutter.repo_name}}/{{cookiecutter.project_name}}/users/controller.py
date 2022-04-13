from typing import List, Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from {{cookiecutter.project_name}}.core.binding import Container
from {{cookiecutter.project_name}}.users.dto import UserCreationIntention, UserDTO
from {{cookiecutter.project_name}}.users.exceptions import (
    DuplicateUserError,
    UserNotFoundError,
)
from {{cookiecutter.project_name}}.users.model import User
from {{cookiecutter.project_name}}.users.service import UserService

router = APIRouter(prefix="/users", tags=["user-service"])


@router.get("/", name="get-all-users", response_model=List[UserDTO])
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> List[User]:
    return user_service.get_all()


@router.get("/{user_external_id}", response_model=User)
@inject
def get_by_external_id(
    user_external_id: str,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    try:
        return user_service.get_by_external_id(user_external_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create(
    user_intention: UserCreationIntention,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    try:
        return user_service.create(user_intention.to_model())
    except DuplicateUserError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
