from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    class config:
        env_file = ".env"  # read the file .env


settings = Settings()
