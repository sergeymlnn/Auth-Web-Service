import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture(scope="function")
async def client():
  """"Provides async client for E2E-testing"""
  async with AsyncClient(app=app, base_url="http://127.0.0.1:8005") as client:
    yield client
