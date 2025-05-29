import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
import os

basedir = os.path.abspath(os.path.dirname(__file__))

parentdir = os.path.abspath(os.path.join(basedir, os.pardir))

db_path = os.path.join(parentdir, 'app.db')

app.config['HOST'] = '0.0.0.0'
app.config['PORT']=5000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)