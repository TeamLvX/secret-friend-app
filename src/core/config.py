from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str
    debug: bool = False
    aws_region: str
    dynamodb_host: str

    class Config:
        env_file = ".env"

settings = Settings()