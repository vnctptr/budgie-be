from typing import Optional

from beancount.core.getters     import GetAccounts
from beancount.core.realization import realize
from beancount.loader           import load_file

from .UserData import UserData

#TODO: This entire file is hardcoded with the test data.
#      this needs to be changed ASAP (when we have something resembling storage)

def load_user( name ) -> Optional[UserData]:
  """
  Loads a user data from file

  Returns None if not found
  """
  (entries, errors, option_map) = load_file( f"./testdata/{name}.bc" )
  if len(errors) > 0:
    return None

  ret = UserData()
  ret.entries = entries
  ret.real_accounts = realize(entries)

  ( accounts, _ ) = GetAccounts().get_accounts_use_map(entries)
  for account in accounts:
    ret.accounts.append( account )

  return ret
