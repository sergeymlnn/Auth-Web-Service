from datetime import datetime

from jose import jwt, JWTError

from app.settings import settings


def encode_jwt_token(username: str, **kwargs) -> str:
  """
  Generates a JWT token based on the username and optional kwargs.

  The output JWT token contains the following claims:
    - exp - time in seconds since the Epoch until token in expired;
    - iat - time in seconds since the Epoch when token was generated;
    - sub - username to sign the token for;
    - custom optional kwargs;

  Note: token expiration time is defined in the settings

  :param username: username to sign the token for to be placed into the payload
  :param kwargs: optional custom arguments to be added to the payload
  :return: a JWT token, signed for the user
  """
  token_created_at = int(datetime.now().strftime("%s"))
  token_expires_at = token_created_at + (settings.jwt_token_expiration_period * 60)
  payload = {
    **kwargs,
    "exp": token_expires_at,
    "iat": token_created_at,
    "sub": username,
  }
  token = jwt.encode(payload, settings.jwt_secret_key, settings.jwt_signing_algorithm)
  return token


def decode_jwt_token(token: str) -> dict[str, str]:
  """
  Decodes the JWT token and returns its payload.

  :param token: a JWT token to decode and return the payload from
  :raises JWTError: if token is expired, corrupted or secret key and/or signing algo are valid
  :return: payload of the token
  """
  try:
    payload = jwt.decode(
      token,
      key=settings.jwt_secret_key,
      algorithms=[settings.jwt_signing_algorithm]
    )
  except JWTError:
    raise
  return payload
