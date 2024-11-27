from os.path import join, dirname, abspath
from os import getenv
from pydantic import BaseSettings
from dotenv import load_dotenv
from common.secret_manager import SecreteData

env_file = join(dirname(abspath(__file__)), ".env")
load_dotenv(env_file, override=True)
key = SecreteData()


class Settings(BaseSettings):
    """
    Use this class for adding constants
    """

    app_name: str = "ADMIN APP"
    docs_url: str = getenv("swagger_url")
    redoc_url: str = getenv("doc_url")
    openapi_url: str = getenv("openapi_url")
    server_timeout: int = int(key.FAST_API_SERVER_TIMEOUT)
    port: int = int(getenv("port"))


settings = Settings()
