from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    app_name: str = Field(default="Secret Friend App")
    env: str = Field(default="development")
    debug: bool = Field(default=False)
    dynamodb_host: str | None = Field(validation_alias="DYNAMODB_ENDPOINT", default=None)
    aws_region: str = Field(default="us-east-1")
    aws_access_key_id: str | None = None
    aws_secret_access_key: str | None = None

    # CORS Configuration
    cors_origins: list[str] = Field(default=["http://localhost:3000"], description="Allowed CORS origins")
    cors_allow_credentials: bool = Field(default=True, description="Allow credentials in CORS requests")
    cors_allow_methods: list[str] = Field(default=["*"], description="Allowed HTTP methods for CORS")
    cors_allow_headers: list[str] = Field(default=["*"], description="Allowed headers for CORS")

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, v):
        if v == "" or v is None:
            return False
        if isinstance(v, str):
            return v.lower() in ("true", "1", "yes", "on")
        return bool(v)


settings = Settings()
