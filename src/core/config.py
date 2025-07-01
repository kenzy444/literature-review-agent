from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    Hugging_face_key: str = ""
    chunk_size: int = 512

    class config:
        env_file = ".env"  # read the file .env


settings = Settings()
