import budgie.verify_config as verify

# example config to be used (not modified) in tests
config = {
  "str": "hello world",
  "int": 42,
  "float": 42.42,
  "obj": {
    "foo": 42,
    "bar": "hello world"
  }
}

#-------------------------------------------------------------------------------

def test_verify_object():
  assert not verify.object(config, "NONEXISTANT")
  assert not verify.object(config, "str")
  assert not verify.object(config, "int")
  assert not verify.object(config, "float")
  assert verify.object(config, "obj")

#-------------------------------------------------------------------------------

def test_verify_integer():
  assert not verify.integer(config, "NONEXISTANT")
  assert not verify.integer(config, "str")
  assert not verify.integer(config, "float")
  assert not verify.integer(config, "obj")

  assert verify.integer(config, "int")
  assert verify.integer(config, "int", min=42)
  assert verify.integer(config, "int", max=43)
  assert verify.integer(config, "int", min=10, max=50)
  assert not verify.integer(config, "int", min=43)
  assert not verify.integer(config, "int", max=42)
  assert not verify.integer(config, "int", min=50, max=60)

  obj = config["obj"]
  assert verify.integer(obj, "foo", "obj")

#-------------------------------------------------------------------------------

def test_verify_number():
  assert not verify.number(config, "NONEXISTANT")
  assert not verify.number(config, "str")
  assert not verify.number(config, "obj")

  assert verify.number(config, "int")
  assert verify.number(config, "float")

  obj = config["obj"]
  assert verify.number(obj, "foo", "obj")
