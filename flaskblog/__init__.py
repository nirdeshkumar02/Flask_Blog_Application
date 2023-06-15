# Importing the Flask class and Setting Up the app variable as an instance of Flask class
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting Secret Configuration for external attacks.
app.config['SECRET_KEY'] = "3d6e044ffd997a7be3e38d017453be94"

# Setting up the SQL Like DB which used as file system.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create a db instance
db = SQLAlchemy(app)

from flaskblog import routes