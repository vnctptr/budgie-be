from typing import (
  Dict,
  List
)


from .io import load_user
from .UserData import UserData

users: Dict[ str, UserData ] = {}

def get_user( name: str ) -> UserData:
  """
  Gets the data for a given user name.

  If the user doesn't exist, throws a LookupError
  """
  if name not in users:
    users[name] = load_user(name)

  return users[name]
