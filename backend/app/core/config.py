from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]
BACKEND_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    DATABASE_URL: str

    @property
    def async_database_url(self) -> str:
        url = self.DATABASE_URL
        if "+asyncpg" not in url:
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        if not self.RUNNING_IN_DOCKER:
            url = url.replace("@db:", "@localhost:")
        return url

    RUNNING_IN_DOCKER: bool = False

    model_config = SettingsConfigDict(
        env_file=(PROJECT_ROOT / ".env", BACKEND_ROOT / ".env"),
        extra="ignore",
    )


settings = Settings()
