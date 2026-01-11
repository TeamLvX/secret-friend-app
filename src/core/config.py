from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    app_name: str
    env: str
    debug: bool = False
    aws_region: str = "us-east-1"
    dynamodb_host: str = "http://localhost:8000"


settings = Settings()
