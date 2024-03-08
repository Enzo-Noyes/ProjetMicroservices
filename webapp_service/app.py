from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

# URL des microservices
AUTH_SERVICE_URL = 'http://auth:5002'
GAME_SERVICE_URL = 'http://motus:5003'
SCORE_SERVICE_URL = 'http://score:5001'

@app.route('/')
def index():
    # Afficher la page d'accueil avec le formulaire de connexion
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Récupérer le nom d'utilisateur et le mot de passe du formulaire
    username = request.form['username']
    password = request.form['password']

    # Vérification des informations d'identification auprès du service d'authentification
    auth_response = requests.post(f'{AUTH_SERVICE_URL}/auth/login', json={'username': username, 'password': password})
    if auth_response.status_code != 200:
        # Si les informations sont invalides, afficher une erreur
        return render_template('index.html', error='Invalid username or password')

    # Rediriger vers la page du jeu avec le nom d'utilisateur
    return redirect(url_for('game', username=username))

@app.route('/game')
def game():
    # Récupérer le nom d'utilisateur de la requête
    username = request.args.get('username')
    if not username:
        # Si le nom d'utilisateur n'est pas transmis, rediriger vers la page d'accueil
        return redirect(url_for('index'))
    # Afficher la page du jeu avec le formulaire pour soumettre un mot
    return render_template('game.html', username=username)

@app.route('/play', methods=['POST'])
def play():
    # Récupérer le nom d'utilisateur et le mot du formulaire
    username = request.form.get('username')
    word = request.form.get('word')

    # Vérifier si 'word' est présent
    if not word:
        return render_template('result.html', message='No word submitted.', username=username)

    # Jouer au jeu (soumettre le mot) auprès du service de jeu
    game_response = requests.post(f'{GAME_SERVICE_URL}/motus/guess', json={'word': word})
    if game_response.status_code == 200:
        message = 'Congratulations! You guessed the word correctly.'
    else:
        message = 'Sorry, the word is incorrect.'

    return render_template('result.html', message=message, username=username)

if __name__ == '__main__':
    # Démarrer l'application sur le port 5004
    app.run(host='0.0.0.0', port=5004, debug=True)
