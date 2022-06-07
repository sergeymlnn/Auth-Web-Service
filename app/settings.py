from pydantic import BaseSettings, Field


class Settings(BaseSettings):
  """Defines settings of the application, using ENV-variables or default values"""
  api_uri: str = Field("http://127.0.0.1:8000", env="API_URI")
  jwt_schema: str = Field("Bearer", env="JWT_SCHEMA")
  jwt_signing_algorithm: str = Field(
    default="HS256",
    env="JWT_SIGNING_ALGORITHM",
    description="JWT signing algorithm"
  )
  jwt_token_expiration_period: int = Field(
    default=1,
    env="JWT_TOKEN_EXPIRATION_PERIOD",
    description="Minutes"
  )
  jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")


settings = Settings()
