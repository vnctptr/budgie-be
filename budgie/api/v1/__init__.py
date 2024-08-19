from flask import Blueprint

api = Blueprint('v1', __name__)

@api.route("/")
def root():
  return "<h1>Hello world</h1>"
