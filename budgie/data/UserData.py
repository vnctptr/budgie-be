from typing import List

from .Account import AccountList

class UserData:
  """
  Contans all data related to a given user
  """

  def __init__( self ):
    """
    Constructor
    """
    self.accounts = AccountList()
