import uvicorn

from app.configs.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "application:get_app",
        workers=settings.workers_count,
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.reload,
        factory=True,
    )


if __name__ == "__main__":
    main()
