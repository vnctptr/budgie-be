from flask import Flask

import argparse
import tomllib

from .util import die

from .api.v1 import api as v1
from .ssh import SSHServer
from .data import DataStorage

# ==============================================================================
# Helper functions
# ==============================================================================

def verify_config(config: dict) -> bool:
  """
  Verifies that the configuration is valid.
  """
  if not SSHServer.verify_config(config):
    return False
  if not DataStorage.verify_config(config):
    return False
  return True

# ==============================================================================
# Arguments and configuration files
# ==============================================================================

parser = argparse.ArgumentParser(
  prog="budgie",
  description="Back-end for budgie"
)
parser.add_argument( "config_file", help="Configuration file to use" )
args = parser.parse_args()

try:
  with open(args.config_file, "rb") as f:
    config = tomllib.load(f)
except FileNotFoundError:
  die(f"Cannot read config file '{args.config_file}'")

if not verify_config(config):
  die(f"Invalid configuration")

# ==============================================================================
# Configure servers
# ==============================================================================

ssh = SSHServer(config)
data = DataStorage(config)

app = Flask("budgie-be")
app.register_blueprint( v1, url_prefix='/v1', data_obj=data )

# ==============================================================================
# Main script
# ==============================================================================
if __name__ == "__main__":
  ssh.start()
  app.run()
  ssh.stop()
