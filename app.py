from flask import Flask, request, jsonify

app = Flask(__name__)
USERS = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing credentials'}), 400
    if data['username'] in USERS:
        return jsonify({'error': 'User already exists'}), 409
    USERS[data['username']] = data['password']
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid credentials'}), 400
    if USERS.get(data['username']) == data['password']:
        return jsonify({'token': 'fake-jwt-token'}), 200
    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/dashboard', methods=['GET'])
def dashboard():
    auth = request.headers.get('Authorization')
    if auth != 'Bearer fake-jwt-token':
        return jsonify({'error': 'Forbidden'}), 403
    return jsonify({'message': 'Welcome to your dashboard!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
