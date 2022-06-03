from pydantic import BaseSettings, Field


class Settings(BaseSettings):
  """Defines settings of the application, using ENV-variables or default values"""
  api_uri: str = Field("http://127.0.0.1:8000", env="API_URI")


settings = Settings()
