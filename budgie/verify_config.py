from typing import Optional

from .util import error

def _make_path(prop: str, path: Optional[str]) -> str:
  """
  Completes a path to be printed.
  """
  if path is None:
    return prop
  else:
    return f"{path}.{prop}"

#-------------------------------------------------------------------------------

def object(
    config: dict,
    prop:   str,
    path:   Optional[str] = None) -> bool:
  """
  Makes sure that config[prop] exists and is an object

  Prints a message to stderr if it is wrong.

  Args:
    - config: dictionary containing the configuration to be tested
    - prop: property to search for
    - path: parent path of "config" in the main configuration file, for proper
            error message handling

  Returns:
    - True if the config[prop] exists (no message printed to stderr)
    - False if it does not exist (message will be printed to stderr)
  """
  if prop not in config:
    error(f"Missing {_make_path(prop, path)} (object).")
    return False
  if not isinstance(config[prop], dict):
    error(f"{_make_path(prop, path)} is not an object.")
    return False
  return True

#-------------------------------------------------------------------------------

def integer(
    config: dict,
    prop:   str,
    path:   Optional[str] = None,
    *,
    min:    Optional[int] = None,
    max:    Optional[int] = None) -> bool:
  """
  Makes sure that config[prop] exists and is an integer

  Prints a message to stderr if it is wrong.

  Args:
    - config: dictionary containing the configuration to be tested
    - prop: property to search for
    - path: parent path of "config" in the main configuration file, for proper
            error message handling
    - min: minimum value accepted (inclusive)
    - max: maximum value accepted (exclusive)

  Returns:
    - True if the config[prop] exists (no message printed to stderr)
    - False if it does not exist (message will be printed to stderr)
  """
  spec = ""
  if min is not None and max is not None:
    spec = f" > {min} <= {max}"
  elif min is not None:
    spec = f" > {min}"
  elif max is not None:
    spec = f" <= {max}"

  if prop not in config:
    error(f"Missing {_make_path(prop, path)} (integer{spec}).")
    return False
  if not isinstance(config[prop], int):
    error(f"{_make_path(prop, path)} is not an integer{spec}.")
    return False
  v = config[prop]
  ok = True
  if min is not None and v < min:
    ok = False
  if max is not None and v >= max:
    ok = False
  if not ok:
    error(f"{_make_path(prop, path)} should be{spec}")
    return False
  return True

#-------------------------------------------------------------------------------

def number(
    config: dict,
    prop:   str,
    path:   Optional[str] = None) -> bool:
  """
  Makes sure that config[prop] exists and is a number

  Prints a message to stderr if it is wrong.

  Args:
    - config: dictionary containing the configuration to be tested
    - prop: property to search for
    - path: parent path of "config" in the main configuration file, for proper
            error message handling

  Returns:
    - True if the config[prop] exists (no message printed to stderr)
    - False if it does not exist (message will be printed to stderr)
  """
  if prop not in config:
    error(f"Missing {_make_path(prop, path)} (number).")
    return False
  ok = False
  for type in [int, float]:
    if isinstance(config[prop], type):
      ok = True
  if not ok:
    error(f"{_make_path(prop, path)} is not a number.")
    return False
  return True
