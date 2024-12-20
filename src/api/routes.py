"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def handle_create_user():
    email = request.get_json()['email']
    password = request.get_json()['password']

    if email is None or password is None:
        return jsonify({'error': 'Missing email or password'}), 400
    
    new_user= User()
    new_user.email = email
    new_user.password = password
    new_user.is_active = True

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'id' : new_user.id }), 200

@api.route('/login', methods=['POST'])
def handle_login():
    email = request.get_json()['email']
    password = request.get_json()['password']

    if email is None or password is None:
        return jsonify({'error': 'Incorrect credentials'}), 400
    
    user = User.query.filter_by(email=email, password=password).first()
    
    if user is None:
        return jsonify ({'error': 'user not exist'}), 400
    
    access_token = create_access_token(identity=user.email)

    return jsonify ({'id': user.id, 'access_token': access_token}), 200

@api.route('/private', methods=['GET'])
@jwt_required()
def handle_user_private():
    current_user_email = get_jwt_identity()

    user = User.query.filter_by(email=current_user_email).first()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "email": user.email,
        "message": "Welcome to private!"
    }), 200