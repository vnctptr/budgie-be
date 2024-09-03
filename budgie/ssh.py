from typing import List

import paramiko as ssh

class SSHServer:
  """
  Serves the git repositories to incoming clients.
  """

  def __init__( self, host: str ):
    """
    Constructor.

    Args:
      - Host: hostname with optional port (separated by ":")
    """
    self.ssh_transport = ssh.transport.Transport(host)

  #-----------------------------------------------------------------------------

  def start( self ):
    """
    Starts the server and begin accepting clients.
    """
    self.ssh_transport.start_server(server=self)

  #-----------------------------------------------------------------------------

  def stop( self ):
    """
    Stops the server.
    """

  #-----------------------------------------------------------------------------

  def get_allowed_auths( self ) -> List[str]:
    """
    Overwritten from paramiko SSH server
    """
    return ["publickey"]

  #-----------------------------------------------------------------------------

  def check_auth_none( self, username: str ) -> int:
    """
    Checks if a given username is allowed to open a channel without auth.

    Overwritten from paramiko SSH server

    Since we only accept publickey authentication, this will always return fail.
    """
    return ssh.AUTH_FAILED

  #-----------------------------------------------------------------------------

  def check_auth_password( self ):
    """
    Checks if a given username and password is acceptable.

    Overwritten from paramiko SSH server.

    Since we only accept publickey authentication, this will always return fail.
    """
    return ssh.AUTH_FAILED

  #-----------------------------------------------------------------------------

  def check_auth_publickey( self ):
    """
    Checks if a given public key is acceptable for authentication.

    Overwritten from paramiko SSH server.
    """
    #FIXME: we are missing some checks for acceptable ssh keys
    return ssh.AUTH_SUCCESSFUL
