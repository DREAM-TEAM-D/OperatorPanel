from flask import Flask, jsonify, request, json, render_template
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from pyfladesk import init_gui


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lelelelel'
app.config['MYSQL_DB'] = 'db_operatorpanel'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

@app.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    cur.execute("SELECT * FROM op_users where email = '" + str(email) + "'")
    rv = cur.fetchone()

    if bcrypt.check_password_hash(rv['password'], password):
        access_token = create_access_token(
            identity={
                'first_name': rv['first_name'],
                'last_name': rv['last_name'],
                'email': rv['email']
            })
        result = access_token
    else:
        result = jsonify({"error": "Invalid username and password"})

    return result

if __name__ == "__main__": 
	app.run()