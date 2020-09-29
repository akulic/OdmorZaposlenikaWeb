from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '9e0d1340ba0c67cf242ed8a24423d611'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///odmorzap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from odmor import routes