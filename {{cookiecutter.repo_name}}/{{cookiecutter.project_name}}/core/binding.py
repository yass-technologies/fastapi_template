from dependency_injector import containers, providers

from {{cookiecutter.project_name}}.core.config import settings
from {{cookiecutter.project_name}}.misc.sql_database.database import Database
from {{cookiecutter.project_name}}.users.repository import UserRepository
from {{cookiecutter.project_name}}.users.service import UserService

WIRED_MODULES = ["{{cookiecutter.project_name}}.users.controller"]


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=WIRED_MODULES)

    db: providers.Singleton[Database] = providers.Singleton(
        Database, db_url=config.db.db_url
    )

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
