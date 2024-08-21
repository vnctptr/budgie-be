from typing import (
  Dict,
  Optional
)

from .io import load_user
from .UserData import UserData

users: Dict[ str, UserData ] = {}

def get_user( name: str ) -> Optional[ UserData ]:
  """
  Gets the data for a given user name.

  If the user doesn't exist, returns None
  """
  if name in users:
    return users[name]

  user = load_user(name)
  if user is None:
    return None

  users[name] = user
  return user
