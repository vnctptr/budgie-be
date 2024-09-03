import pygit2

class Storage:
  """
  Stores data for a given user as a git repository.
  """

  def __init__( self, user: str ):
    """
    Constructor.
    """

