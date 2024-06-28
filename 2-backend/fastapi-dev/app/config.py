import logging
import os

from typing import Literal
from pydantic_settings import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: Literal["dev", "stage", "prod"] = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    API_PREFIX: str = "/api"
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "Visual IDMA Service"
    DEBUG: bool = os.getenv("DEBUG", default=False)

    # Authentication
    API_CLIENT_ID: str = os.getenv("API_CLIENT_ID", default="")
    API_CLIENT_SECRET: str = os.getenv("API_CLIENT_SECRET", default="")
    SWAGGER_UI_CLIENT_ID: str = os.getenv("SWAGGER_UI_CLIENT_ID", default="")
    AAD_TENANT_ID: str = os.getenv("AAD_TENANT_ID", default="")

    AAD_INSTANCE: str = os.getenv("AAD_INSTANCE", default="https://login.microsoftonline.com")
    API_AUDIENCE: str = os.getenv("API_AUDIENCE", default=f"api://{API_CLIENT_ID}")

def get_settings() -> BaseSettings:
    log.info("Loading config settings from env")
    return Settings()
