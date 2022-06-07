from pydantic import BaseSettings

class Settings(BaseSettings):
    BASE_URL: str= "https://frontend-hireable.vercel.app"


settings = Settings()