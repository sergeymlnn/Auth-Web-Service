from datetime import datetime
from time import sleep

import pytest
from jose import JWTError

from app.settings import settings
from app.services.jwt import encode_jwt_token, decode_jwt_token


DEFAULT_USER_INFO = [
  ("john", {}),
  ("helen", {"email": "helen@example.com"}),
]


@pytest.mark.parametrize("username, custom_payload", DEFAULT_USER_INFO)
def test_encode_jwt_token(username, custom_payload):
  """Validates generated JWT and its claims 'username' + optional custom payload"""
  token = encode_jwt_token(username, **custom_payload)
  assert token
  decoded_token = decode_jwt_token(token)
  assert decoded_token["sub"] == username
  assert decoded_token.get("email") == custom_payload.get("email")


@pytest.mark.parametrize("username, custom_payload", DEFAULT_USER_INFO)
def test_encode_jwt_token_verify_token_payload(username, custom_payload):
  """Validates 'iat' and 'exp' claims of the JWT token"""
  token = encode_jwt_token(username, **custom_payload)
  token_created_at = int(datetime.now().strftime("%s"))
  token_expires_at = token_created_at + (settings.jwt_token_expiration_period * 60)
  decoded_token = decode_jwt_token(token)
  assert decoded_token["iat"] == token_created_at
  assert decoded_token["exp"] == token_expires_at
  assert decoded_token.get("email") == custom_payload.get("email")


@pytest.mark.parametrize("username", ["lincoln"])
def test_decode_jwt_token_wrong_secret_key(monkeypatch, username):
  """Verifies exception and its message, once the secret key to decode the JWT token is corrupted"""
  token = encode_jwt_token(username)
  with monkeypatch.context() as m, pytest.raises(JWTError) as e:
    m.setattr(settings, "jwt_secret_key", "123")
    decode_jwt_token(token)
  assert str(e.value) == "Signature verification failed."


@pytest.mark.parametrize("username", ["markus"])
def test_decode_jwt_token_wrong_algorithm(monkeypatch, username):
  """Verifies exception and its message, once the algorithm to decode the JWT token is incorrect"""
  token = encode_jwt_token(username)
  with monkeypatch.context() as m, pytest.raises(JWTError) as e:
    m.setattr(settings, "jwt_signing_algorithm", settings.jwt_signing_algorithm + "AAA")
    decode_jwt_token(token)
  assert str(e.value) == "The specified alg value is not allowed"


@pytest.mark.parametrize("username", ["bruneau"])
def test_decode_jwt_token_expired_token(monkeypatch, username):
  """Verifies exception and its message, once the JWT token is expired"""
  with monkeypatch.context() as m:
    m.setattr(settings, "jwt_token_expiration_period", 0)
    token = encode_jwt_token(username)
    sleep(1)
    with pytest.raises(JWTError) as e:
      decode_jwt_token(token)
  assert str(e.value) == "Signature has expired."


@pytest.mark.parametrize(
  "token, error_message",
  [
    ("", "Not enough segments"),
    ("qwerty", "Not enough segments"),
    (f"{encode_jwt_token('dan')}1", "Signature verification failed."),
  ]
)
def test_decode_jwt_token_wrong_token(token, error_message):
  """Verifies exception and its message, once the JWT token is not a valid JWT token"""
  with pytest.raises(JWTError) as e:
    decode_jwt_token(token)
  assert str(e.value) == error_message
