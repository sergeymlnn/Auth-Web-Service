from time import time


def current_time() -> int:
  """Returns the current time in seconds, rounding value to the integer"""
  return int(time())
