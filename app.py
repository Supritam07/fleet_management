import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from logging.config import dictConfig
from settings import settings
from config.openapi_schema import Open_api_AppConstants
from routers import ENDPOINTS
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(env_file, override=True)
APP_ENDPOINTS = []


def custom_openapi(apps: FastAPI):
    if apps.openapi_schema:
        return apps.openapi_schema
    openapi_schema = get_openapi(
        title="FLEET MANAGER (BACKEND APIS)",
        version="1.0",
        description="These APIs are used to support FLEET MANAGER functionalities:",
        routes=apps.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": Open_api_AppConstants.TRUCK_LOGO
    }
    apps.openapi_schema = openapi_schema
    return apps.openapi_schema


def configure_routes(apps: FastAPI) -> None:
    """
    Register the routers on the application instance.
    Routers are objects that map url routes to our python functions.
    This will be used to register all the endpoints of the application.
    """
    APP_ENDPOINTS.extend(ENDPOINTS)

    for endpoint in APP_ENDPOINTS:
        apps.include_router(endpoint.router, prefix=endpoint.prefix)


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        openapi_url=settings.openapi_url,
    )

    # Configure routes
    configure_routes(app)

    # Set custom OpenAPI
    app.openapi = lambda: custom_openapi(app)

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


# The main app instance creation can now be simplified
app = create_app()
