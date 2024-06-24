import logging
import os

from typing import Literal
from pydantic_settings import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: Literal["dev", "stage", "prod"] = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings() -> BaseSettings:
    log.info("Loading config settings from env")
    return Settings()
