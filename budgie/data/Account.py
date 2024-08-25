from typing import Dict, List, Optional, Union

class Account:
  """
  Represents an account name.

  Accounts are strings, separated by colons. E.g. "Expenses:Home:Electricity",
  "Expenses:Home:Phone" and "Expenses:Home:Internet"

  These account names are split at the colon and made into a path.
  """

  def __init__( self, name: str ):
    """
    Constructs an account from an account name.
    """
    self.account = str.split(name, ":")


  def __str__( self ) -> str:
    """
    Returns the account name as a string
    """
    return ":".join( self.account )


  def __repr__( self ) -> str:
    """
    Returns the representation of the account name
    """
    return f'Account("{self.__str__()}")'


  def __eq__( self, value: Union[ str, 'Account'] ) -> bool:
    """
    Returns true if self and value represent the same account
    """
    if isinstance( value, str ):
      value = Account(value)

    if len( self.account ) != len( value.account ):
      return False

    for i in range( len(self.account) ):
      if self.account[i] != value.account[i]:
        return False

    return True


  def empty( self ) -> bool:
    """
    Returns true if there is no account name specified
    """
    return len( self.account ) == 0


  def push_front( self, value: Union[ str, 'Account' ] ):
    """
    Adds an account to the beginning of this.
    """
    if isinstance( value, str ):
      value = Account(value)

    new_account = value.account

    for val in self.account:
      new_account.append( val )

    self.account = new_account


  def push_back( self, value: Union[ str, 'Account' ] ):
    """
    Adds an account to the end of this.
    """
    if isinstance( value, str ):
      value = Account(value)

    for val in value.account:
      self.account.append( val )


  def pop_front( self ) -> str:
    """
    Removes the first subaccount from this and returns it.
    """
    return self.account.pop(0)


  def pop_back( self ) -> str:
    """
    Removes the last subaccount from this and returns it.
    """
    return self.account.pop(-1)

#-------------------------------------------------------------------------------

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


  def append( self, account: Union[ str, Account ] ):
    """
    Adds an account to the list of accounts.

    Args:
      account: an account name, either as a string (e.g. "foo:bar:baz")
               or as a list of strings (e.g. ["foo", "bar", "baz"])
    """
    if isinstance( account, str ):
      account = Account(account)

    assert not account.empty()
    root = account.pop_front()
    if root in self.accounts:
      lower_list = self.accounts[root]
    else:
      lower_list = AccountList()

    if( not account.empty() ):
      lower_list.append( account )

    self.accounts[root] = lower_list


  def contains( self, account: Union[ str, Account ]) -> bool:
    """
    Returns true if the account is already in the account list
    """
    if isinstance( account, str ):
      account = Account(account)

    if account.empty():
      return True

    root = account.pop_front()
    if root not in self.accounts:
      return False

    return self.accounts[root].contains( account )


  def list_accounts( self ) -> List[ Account ]:
    """
    Return a list of all accounts, ordered alphabetically
    """
    ret: List[Account] = []

    for root in self.accounts:
      ret.append( Account(root) )
      subaccounts = self.accounts[root].list_accounts()
      for subaccount in subaccounts:
        subaccount.push_front( root )
        ret.append( subaccount )

    ret.sort()
    return ret
