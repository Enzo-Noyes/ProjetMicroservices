from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionnaire pour stocker les informations des utilisateurs
users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Vérifie si les informations d'identification sont correctes
    if username in users and users[username] == password:
        response = {'message': 'Connexion réussie !'}
    else:
        response = {'message': 'Identifiants incorrects.'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002,debug=True)
