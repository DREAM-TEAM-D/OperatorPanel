from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Create an Instance of Flask
app = Flask(__name__)

#Include config from config.py
app.config.from_object('config')
app.secret_key = 'some_secret'

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

import Operator_Panel.views
