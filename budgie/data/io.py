import beancount as bc

from .UserData import UserData

#TODO: This entire file is hardcoded with the test data.
#      this needs to be changed ASAP (when we have something resembling storage)

def load_user( name ) -> UserData:
  """
  Loads a user data from file
  """
  (entries, errors, option_map) = bc.loader.load_file(
    f"./testdata/{name}.bc"
  )
  if len(errors) > 0:
    raise LookupError

  return UserData()
