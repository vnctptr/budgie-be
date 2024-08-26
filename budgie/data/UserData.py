from .Account import AccountList

from beancount.core.realization import RealAccount

class UserData:
  """
  Contans all data related to a given user
  """

  def __init__( self ):
    """
    Constructor
    """
    self.entries = []
    self.accounts = AccountList()
    self.real_accounts = RealAccount("")
