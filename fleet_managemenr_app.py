import uvicorn
from app import settings


def run_app():
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=settings.port,
        timeout_keep_alive=settings.server_timeout,
        reload=False,
    )


if __name__ == "__main__":
    run_app()
