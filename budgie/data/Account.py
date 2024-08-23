from typing import Dict, List, Optional, Union

type SplitAccount = List[ str ]

def split_account( account: str ) -> SplitAccount:
  """
  Splits an account name into its parts.

  Args:
    account: an account name as a string (e.g. "foo:bar:baz")

  Return:
    The same account name, split into its parts (e.g. ["foo", "bar", "baz"])
  """
  return str.split(account, ":")


class AccountList:
  """
  Represents a set of account names.

  Accounts are strings, separated by colons. E.g. "Expenses:Home:Electricity",
  "Expenses:Home:Phone" and "Expenses:Home:Internet"

  In addition to these "leaf" accounts, intermediate accounts also need to be
  taken into account (e.g. "Expenses" and "Expenses:Home" in this example).

  We represent all these accounts as a tree, where each level contains one part
  of the account name (e.g. "Expenses" on level 0, "Home" on level 1, etc.)
  """

  def __init__( self, accounts: Optional[List[str]] = None ):
    """
    Constructs an account list.

    Args:
      accounts: list of strings containing account names (e.g. "foo:bar:baz")
    """
    self.accounts: Dict[ str, 'AccountList' ] = {}


    if accounts is not None:
      for account in accounts:
        self.append(account)


  def __str__( self ) -> str:
    """
    Returns the string representation of this object
    """
    ret = '{'
    first = True
    for account in self.accounts:
      if first:
        first = False
      else:
        ret += ", "
      ret += f'"{account}": ' + self.accounts[account].__str__()
    ret += '}'
    return ret


  def append( self, account: Union[ str, SplitAccount ] ):
    """
    Adds an account to the list of accounts.

    Args:
      account: an account name, either as a string (e.g. "foo:bar:baz")
               or as a list of strings (e.g. ["foo", "bar", "baz"])
    """
    if isinstance( account, str ):
      self.append( split_account(account) )
    else:
      assert len(account) > 0
      root = account[0]
      if root in self.accounts:
        lower_list = self.accounts[root]
      else:
        lower_list = AccountList()

      account.pop(0)
      if( len(account) > 0):
        lower_list.append( account )

      self.accounts[root] = lower_list


  def contains( self, account: Union[ str, SplitAccount ]) -> bool:
    """
    Returns true if the account is already in the account list
    """
    if isinstance( account, str ):
      return self.contains( split_account(account) )
    else:
      if len(account) < 1:
        return True

      root = account[0]
      if root not in self.accounts:
        return False

      account.pop(0)
      return self.accounts[root].contains( account )
