from typing import Optional

from flask import Blueprint, abort
from flask.blueprints import BlueprintSetupState

from budgie.data import DataStorage

# ==============================================================================
# Constants & global variables
# ==============================================================================

MAX_ACCOUNT_PATH_LENGTH = 5

api = Blueprint('v1', __name__)
_data: Optional[DataStorage] = None

# ==============================================================================
# API initialization
# ==============================================================================

def api_init(state: BlueprintSetupState):
  """
  Initializes the API
  """
  global _data
  assert "data_obj" in state.options
  _data = state.options["data_obj"]

api.record(api_init)

# ==============================================================================
# Test routes
# ==============================================================================

@api.route("/")
def root():
  return "<h1>Hello world</h1>"

# ==============================================================================
# Accounts
# ==============================================================================

@api.route("/users/<name>/accounts/")
def get_account_list( name: str ):
  """
  List all accounts for a given user

  Args:
    name: user name to list accounts for
  """
  global _data
  assert _data is not None

  user = _data.get_user(name)
  if user is None:
    abort(404)

  return {
    "accounts": user.accounts.to_dict(),
    "balance": user.real_accounts.balance
  }

# ------------------------------------------------------------------------------

def get_account( name: str, **kwargs ):
  """
  Gets a single account for a given user

  Args:
    name: user name to list accounts for
    kwargs: breadcrumbs to reconstitute account name from
  """
  global _data
  assert _data is not None

  user = _data.get_user(name)
  print(user)
  if user is None:
    abort(404)

  account_name = ""

  for depth in range( MAX_ACCOUNT_PATH_LENGTH ):
    var = f"breadcrumb_{depth}"
    if var in kwargs:
      if account_name == "":
        account_name = kwargs[var]
      else:
        account_name = f"{account_name}:{kwargs[var]}"
    else:
      break

  account = user.accounts.get(account_name)
  if account is None:
    abort(404)

  return {
    "name": account_name,
    "accounts": account.to_dict()
  }

# register URL rules for all path depths supported
rule = "/users/<name>/accounts/"
for depth in range( MAX_ACCOUNT_PATH_LENGTH ):
  rule = f"{rule}<breadcrumb_{depth}>/"
  api.add_url_rule(rule, view_func=get_account)
