"""Server for movie ratings app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
