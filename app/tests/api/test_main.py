import pytest


@pytest.mark.anyio
async def test_main(client):
  """Test for '/' route"""
  response = await client.get("/")
  assert response.status_code == 200
  assert response.json()["response"] == "hello, world"
