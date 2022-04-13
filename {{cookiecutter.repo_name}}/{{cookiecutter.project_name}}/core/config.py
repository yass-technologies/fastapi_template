from __future__ import annotations

import logging
import os
from enum import Enum

from dotenv import load_dotenv
from pydantic import BaseConfig

PROJECT_NAME = "{{cookiecutter.project_name}}"
API_VERSION = "1"
API_PREFIX = f"/api/v{API_VERSION}"

load_dotenv()  # take environment variables from .env.
origins = ["*"]


class Environment(Enum):
    PROD = 0
    DEV = 1
    STAGING = 2

    @staticmethod
    def from_str(label: str) -> Environment:
        if label is not None:
            if label.upper() in ("PROD", "PRODUCTIVE"):
                return Environment.PROD
            elif label.upper() in ("STG", "STAGING"):
                return Environment.STAGING
        return Environment.DEV

    @staticmethod
    def get_log_level(environment: Environment) -> int:
        if environment == Environment.DEV:
            return logging._nameToLevel["DEBUG"]
        return logging._nameToLevel["INFO"]


class AppConfig(BaseConfig):

    environment: Environment = Environment.from_str(os.getenv("ENV", ""))

    base_url: str = os.getenv("BASE_URL", "http://127.0.0.1")
    port: str = os.getenv("PORT", "8080")

    logger_name = "app_logger"
    logger_level: int = Environment.get_log_level(environment)

    db_url = os.getenv("DATABASE_URL")

    def is_productive(self) -> bool:
        return self.environment == Environment.PROD

    def is_staging(self) -> bool:
        return self.environment == Environment.STAGING

    def is_development(self) -> bool:
        return self.environment == Environment.DEV


settings = AppConfig()
