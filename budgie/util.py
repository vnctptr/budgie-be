import sys

def error(msg: str):
  """
  Prints an error message to stderr.
  """
  print(msg, file=sys.stderr)

#-------------------------------------------------------------------------------

def die(msg: str):
  """
  Prints an error message to stderr and exit program.
  """
  error(msg)
  quit()
