from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    app_name: str = Field(default="Secret Friend App")
    env: str = Field(default="development")
    debug: bool = Field(default=False)
    dynamodb_host: str = Field(validation_alias="DYNAMODB_ENDPOINT", default="")
    aws_region: str = Field(default="us-east-1")
    aws_access_key_id: str
    aws_secret_access_key: str

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, v):
        if v == "" or v is None:
            return False
        if isinstance(v, str):
            return v.lower() in ("true", "1", "yes", "on")
        return bool(v)


settings = Settings()
