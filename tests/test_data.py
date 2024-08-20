import pytest
import budgie.data

def test_load_users():
  alice = budgie.data.get_user("alice")
  assert len(alice.accounts) > 0

  bob = budgie.data.get_user("bob")
  assert len(bob.accounts) > 0

  with pytest.raises(LookupError):
    budgie.data.get_user("carl")
