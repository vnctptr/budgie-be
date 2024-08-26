import pytest
import budgie.data

def test_load_users():
  alice = budgie.data.get_user("alice")
  assert alice is not None
  assert alice.accounts.contains("Assets:US:BofA:Checking")

  bob = budgie.data.get_user("bob")
  assert bob is not None
  assert alice.accounts.contains("Assets:US:BofA:Checking")

  carl = budgie.data.get_user("carl")
  assert carl is None
