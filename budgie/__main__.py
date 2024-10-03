from flask import Flask

import argparse
import tomllib

from .api.v1 import api as v1
from .ssh import SSHServer

# ==============================================================================
# Arguments and configuration files
# ==============================================================================

parser = argparse.ArgumentParser(
  prog="budgie",
  description="Back-end for budgie"
)
parser.add_argument( "config_file", help="Configuration file to use" )
args = parser.parse_args()

with open(args.config_file, "rb") as f:
  config = tomllib.load(f)

# ==============================================================================
# Configure servers
# ==============================================================================

app = Flask(__name__)
app.register_blueprint( v1, url_prefix='/v1' )

ssh = SSHServer(config['SSH'])

# ==============================================================================
# Main script
# ==============================================================================
if __name__ == "__main__":
  ssh.start()
  app.run()
  ssh.stop()
