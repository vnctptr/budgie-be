from flask import Flask
from .api.v1 import api as v1

app = Flask(__name__)

app.register_blueprint( v1, url_prefix='/v1' )

if __name__ == "__main__":
  app.run()
