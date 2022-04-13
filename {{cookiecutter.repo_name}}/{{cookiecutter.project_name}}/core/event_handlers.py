import logging
from typing import Callable

from fastapi import FastAPI, HTTPException, Request

from {{cookiecutter.project_name}}.core.api_error import AppError
from {{cookiecutter.project_name}}.core.config import settings

logger = logging.getLogger(settings.logger_name)


def start_app_handler(app: FastAPI) -> Callable:
    async def startup() -> None:
        logger.info("Running app start handler.")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    async def shutdown() -> None:
        logger.info("Running app shutdown handler.")

    return shutdown


async def app_exception_handler(request: Request, exc: AppError) -> HTTPException:
    logger.error(
        "There was an error on request: {}".format(extract_log_from_request(request))
    )
    return HTTPException(
        status_code=exc.status_code,
        detail={"message": "Something went wrong"},
    )


def extract_log_from_request(request: Request) -> str:
    return str(request)
