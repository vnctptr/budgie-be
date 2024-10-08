from typing import List

import paramiko as ssh
import socket
import threading

import budgie.verify_config as verify

class SSHServer( ssh.ServerInterface ):
  """
  Serves the git repositories to incoming clients.
  """

  @staticmethod
  def verify_config(main_config: dict) -> bool:
    """
    Verifies that the configuration is valid.
    """
    parent = "SSH"
    if not verify.object(main_config, parent):
      return False
    config = main_config[parent]
    ok = True
    ok &= verify.integer(config, "port", parent, min=0, max=10000)
    return ok

  #-----------------------------------------------------------------------------

  def __init__( self, main_config: dict ):
    """
    Constructor.
    """
    config = main_config["SSH"]

    self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
    self.socket.bind( (socket.gethostname(), config['port']))
    self.socket.listen()

    self.ssh_transport = ssh.transport.Transport(self.socket)

    self.event = threading.Event()

  #-----------------------------------------------------------------------------

  def start( self ):
    """
    Starts the server and begin accepting clients.
    """
    self.ssh_transport.start_server(event=self.event, server=self)

  #-----------------------------------------------------------------------------

  def stop( self ):
    """
    Stops the server.
    """
    self.ssh_transport.stop_thread()

  #-----------------------------------------------------------------------------

  def get_allowed_auths( self ) -> List[str]:
    """
    Overwritten from paramiko SSH server
    """
    return ["publickey"]

  #-----------------------------------------------------------------------------

  def check_auth_none( self, _: str ) -> int:
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
