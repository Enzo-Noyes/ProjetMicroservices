from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionnaire pour stocker les scores des joueurs
scores = {}


@app.route('/score/update', methods=['POST'])
def update_score():
    data = request.get_json()
    player = data.get('player')
    score = data.get('score')

    # Met à jour le score du joueur
    scores[player] = score

    response = {'message': f'Score de {player} mis à jour.'}
    return jsonify(response)


@app.route('/score/rank', methods=['GET'])
def get_rank():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    response = {'rank': sorted_scores}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
