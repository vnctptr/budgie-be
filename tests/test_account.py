from budgie.data.Account import Account, AccountList

def test_Account_basics():
  a1 = Account("foo:bar:baz")
  assert a1.account == ["foo", "bar", "baz"]
  assert str(a1) == "foo:bar:baz"

def test_Account_eq():
  a1 = Account("foo:bar:baz")
  a2 = Account("foo:bar")
  a3 = Account("foo:bar")
  assert a1 != a2
  assert a2 == a3
  assert a1 == "foo:bar:baz"
  assert a2 == "foo:bar"

def test_Account_push():
  a1 = Account( "bar" )
  a1.push_front("foo")
  assert a1 == "foo:bar"
  a1.push_back("baz")
  assert a1 == "foo:bar:baz"
  a1.push_front("test1:test2")
  a1.push_back("test3:test4:test5")
  assert a1 == "test1:test2:foo:bar:baz:test3:test4:test5"

def test_Account_pop():
  a1 = Account("foo:bar:baz")
  assert a1 == "foo:bar:baz"
  assert a1.pop_front() == "foo"
  assert a1 == "bar:baz"
  assert a1.pop_back() == "baz"
  assert a1 == "bar"

def test_AccountList_init():
  var1 = AccountList()
  assert len(var1.accounts) == 0

  var2 = AccountList( ["foo:bar", "foo:baz" ])
  assert len(var2.accounts) == 1
  assert "foo" in var2.accounts
  var3 = var2.accounts["foo"]
  assert isinstance( var3, AccountList )
  assert len(var3.accounts) == 2
  assert "bar" in var3.accounts
  assert "baz" in var3.accounts

def test_AccountList_str():
  var1 = AccountList()
  assert var1.__str__() == "{}"

  var2 = AccountList( ["foo:bar", "foo:baz" ])
  assert var2.__str__() == '{"foo": {"bar": {}, "baz": {}}}'

def test_AccountList_append():
  l = AccountList()
  assert len(l.accounts) == 0
  l.append("foo")
  assert len(l.accounts) == 1
  assert "foo" in l.accounts
  l.append("bar:baz")
  assert len(l.accounts) == 2
  assert "bar" in l.accounts
  l.append("bar")
  assert len(l.accounts) == 2

def test_AccountList_contains():
  l = AccountList()
  assert not l.contains("foo")
  l.append("foo:bar")
  assert l.contains("foo")
  assert l.contains("foo:bar")
  assert not l.contains("bar")
  assert not l.contains("foo:bar:baz")

def test_AccountList_list_accounts():
  l = AccountList()
  assert len( l.list_accounts() ) == 0
  l.append("foo:baz")
  s = l.list_accounts()
  assert len(s) == 2
  assert s[0] == "foo"
  assert s[1] == "foo:baz"
  l.append("foo:bar")
  s = l.list_accounts()
  assert len(s) == 3
  assert s[0] == "foo"
  assert s[1] == "foo:bar" # should be ordered alphabetically
  assert s[2] == "foo:baz"
