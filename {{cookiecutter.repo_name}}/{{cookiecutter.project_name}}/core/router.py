from fastapi import APIRouter

from {{cookiecutter.project_name}}.core.config import API_PREFIX
from {{cookiecutter.project_name}}.core.heartbeat import controller as heartbeat_controller
from {{cookiecutter.project_name}}.users import controller as user_controller

router = APIRouter(prefix=API_PREFIX)

router.include_router(heartbeat_controller.router)
router.include_router(user_controller.router)
