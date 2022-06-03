import pytest
from httpx import AsyncClient

from app.main import app
from app.settings import settings


@pytest.fixture(scope="function")
async def client():
  """"Provides async client for E2E-testing"""
  async with AsyncClient(app=app, base_url=settings.api_uri) as client:
    yield client
