from flask import Flask, request, jsonify

app = Flask(__name__)

# Adresse de base des autres microservices
SCORE_SERVICE_URL = 'http://localhost:5001'
AUTH_SERVICE_URL = 'http://localhost:5002'

# Liste de mots pour le jeu Motus (peut être remplacée par une API externe)
words = ["python", "flask", "docker", "micros", "service"]


@app.route('/motus/guess', methods=['POST'])
def guess_word():
    data = request.get_json()
    word = data.get('word')

    # Vérifie si le mot deviné est correct
    if word in words:
        response = {'message': 'Bravo, vous avez deviné le mot !'}
        # Mise à jour du score du joueur
        update_score(data.get('player'))
    else:
        response = {'message': 'Désolé, le mot est incorrect.'}

    return jsonify(response)


def update_score(player):
    # Appel du microservice de score pour mettre à jour le score du joueur
    payload = {'player': player, 'score': 10}  # Score arbitraire pour l'exemple
    response = requests.post(f'{SCORE_SERVICE_URL}/score/update', json=payload)
    print(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
