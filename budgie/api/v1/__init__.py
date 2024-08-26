from typing import List

from flask import Blueprint, abort

import budgie.data

api = Blueprint('v1', __name__)

# ==============================================================================
# Constants
# ==============================================================================

MAX_ACCOUNT_PATH_LENGTH = 5

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
  user = budgie.data.get_user(name)
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
  user = budgie.data.get_user(name)
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
  print(rule)
  api.add_url_rule(rule, view_func=get_account)
