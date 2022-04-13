import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from {{cookiecutter.project_name}} import __version__
from {{cookiecutter.project_name}}.core import router
from {{cookiecutter.project_name}}.core.api_error import AppError
from {{cookiecutter.project_name}}.core.binding import Container
from {{cookiecutter.project_name}}.core.config import (
    PROJECT_NAME,
    AppConfig,
    origins,
    settings,
)
from {{cookiecutter.project_name}}.core.event_handlers import (
    app_exception_handler,
    start_app_handler,
    stop_app_handler,
)


def get_application(app_config: AppConfig) -> FastAPI:
    logging.basicConfig(
        level=app_config.logger_level,
        format="%(filename)s: "
        "%(levelname)s: "
        "%(funcName)s(): "
        "%(lineno)d:\t"
        "%(message)s",
    )

    is_debug = not app_config.is_productive()
    app = FastAPI(title=PROJECT_NAME, debug=is_debug, version=__version__)

    container = Container()
    container.config.from_yaml("di_config.yaml")

    db = container.db()
    db.create_database()

    app.container = container  # type: ignore

    app.include_router(router.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", start_app_handler(app))
    app.add_event_handler("shutdown", stop_app_handler(app))
    app.add_exception_handler(AppError, app_exception_handler)

    return app


app = get_application(settings)


@app.get("/", tags=["system"], summary="Redirect to /docs")
async def root() -> RedirectResponse:
    """
    Redirect to /docs
    """
    return RedirectResponse(url="/docs")
