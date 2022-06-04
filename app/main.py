from fastapi import FastAPI

from utils import current_time


app = FastAPI()


@app.get("/")
async def main():
  """"""
  return {"response": "hello, world"}


@app.get("/health")
async def health():
  """
  Returns a response with the current time in seconds since the Epoch

  :return: current time in seconds
  """
  return {"response": current_time()}
