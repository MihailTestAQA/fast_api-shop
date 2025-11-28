from email.mime import image
import http
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debag: bool = True
    database_url: str = "sqlite:/// ./shop.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0/0/1:5173",
        "http://127/0/0/1:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/image"

    class Config:
        env_file = ".env"

settings = Settings()
