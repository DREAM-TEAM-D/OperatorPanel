from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'paaassss'
app.config['MYSQL_DB'] = 'db_operatorpanel'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

from app import routes