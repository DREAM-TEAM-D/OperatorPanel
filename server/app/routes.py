from flask import request, jsonify
from app import app, mysql, bcrypt, jwt 
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


@app.route('/users/register', methods=['POST'])
def register():
    cur = mysql.connection.cursor()
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(
        request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    cur.execute(
        "INSERT INTO op_users (first_name, last_name, email, password, created) VALUES ('"
        + str(first_name) + "','" + str(last_name) + "','" + str(email) +
        "','" + str(password) + "','" + str(created) + "')")
    mysql.connection.commit()

    result = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'created': created
    }

    return jsonify({'result': result})

@app.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    email = request.get_json()['email']
    password = request.get_json()['password']

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    cur.execute("SELECT * FROM op_users where email = '" + str(email) + "'")
    rv = cur.fetchone()

    if bcrypt.check_password_hash(rv['password'], password):
        access_token = create_access_token(
            identity={
                'first_name': rv['first_name'],
                'last_name': rv['last_name'],
                'email': rv['email']
            })
        return jsonify({'success': True, 'token': access_token}), 200
    else:
        return jsonify({'success': False, 'message': 'Bad email or password'}), 401


@app.route('/verify-token', methods=['POST'])
@jwt_required
def verify_token():
    return jsonify({'success': True}), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
