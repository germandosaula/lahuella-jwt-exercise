from flask import Flask, request, jsonify, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

CORS(app, origins=["https://stunning-memory-97qxgqw4wr7jfwvr-3000.app.github.dev"])

app.config["JWT_SECRET_KEY"] = "1234"
jwt = JWTManager(app)

api = Blueprint('api', __name__)

@api.route('/hello', methods=['GET'])
def handle_hello():
    response = jsonify({"message": "Hello from the server!"})
    response.headers['Content-Type'] = 'application/json'
    return response, 200

@app.route('/signup', methods=['POST'])
def handle_create_user():
    email = request.get_json().get('email')
    password = request.get_json().get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400
    
    new_user = User()
    new_user.email = email
    new_user.password = password
    new_user.is_active = True

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'id': new_user.id}), 200

@app.route('/login', methods=['POST'])
def handle_login():
    print("Handling login...")
    try:
        email = request.get_json().get('email')
        password = request.get_json().get('password')

        if not email or not password:
            return jsonify({'error': 'Incorrect credentials'}), 400

        print(f"Email received: {email}, Password received: {password}")

        user = User.query.filter_by(email=email, password=password).first()

        if user is None:
            return jsonify({'error': 'User not found'}), 404

        access_token = create_access_token(identity=user.email)

        return jsonify({'id': user.id, 'access_token': access_token}), 200

    except Exception as e:
        print(f"Error in login: {e}")
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/private', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)
