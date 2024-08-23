from budgie.data.Account import split_account, AccountList

def test_split_account():
  assert split_account("foo:bar:baz") == ["foo", "bar", "baz"]

def test_init():
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

def test_str():
  var1 = AccountList()
  assert var1.__str__() == "{}"

  var2 = AccountList( ["foo:bar", "foo:baz" ])
  assert var2.__str__() == '{"foo": {"bar": {}, "baz": {}}}'

def test_append():
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

def test_contains():
  l = AccountList()
  assert not l.contains("foo")
  l.append("foo:bar")
  assert l.contains("foo")
  assert l.contains("foo:bar")
  assert not l.contains("bar")
  assert not l.contains("foo:bar:baz")
