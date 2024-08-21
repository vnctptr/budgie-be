from typing import Optional

import beancount as bc

from .UserData import UserData

#TODO: This entire file is hardcoded with the test data.
#      this needs to be changed ASAP (when we have something resembling storage)

def load_user( name ) -> Optional[UserData]:
  """
  Loads a user data from file

  Returns None if not found
  """
  (entries, errors, option_map) = bc.loader.load_file(
    f"./testdata/{name}.bc"
  )
  if len(errors) > 0:
    return None

  ret = UserData()

  ( accounts, _ ) = bc.core.getters.GetAccounts().get_accounts_use_map(entries)
  for account in accounts:
    ret.accounts.append( account )

  return ret
