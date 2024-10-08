from typing import (
  Dict,
  Optional
)

from .io import load_user
from .UserData import UserData

class DataStorage:
  """
  Interface abstracting access to user data
  """

  @staticmethod
  def verify_config(config: dict) -> bool:
    """
    Verifies that the configuration is valid.
    """
    return True

  #-----------------------------------------------------------------------------

  def __init__(self, config: dict):
    """
    Constructor.
    """
    self.users: Dict[str, UserData] = {}

  #-----------------------------------------------------------------------------

  def get_user(self, name: str) -> Optional[ UserData ]:
    """
    Gets the data for a given user name.

    If the user doesn't exist, returns None
    """
    if name in self.users:
      return self.users[name]

    user = load_user(name)
    if user is None:
      return None

    self.users[name] = user
    return user
