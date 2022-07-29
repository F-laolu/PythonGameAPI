# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
import json


from flask import Flask, jsonify, request

gameScore = Flask(__name__)

gameResults = [
    {'id': "0", 'playerName': "Femi", 'score': "170", 'date': "08/02/2021"},
    {'id': "1", 'playerName': "Ola", 'score': "90", 'date': "22/06/2021"},
    {'id': "2", 'playerName': "Tola", 'score': "150", 'date': "22/07/2021"},
    {'id': "3", 'playerName': "Wale", 'score': "160", 'date': "08/12/2021"},
]


@gameScore.route('/')
def index():
    return "These are the game results data for various players, updated with github."

@gameScore.route("/gameResults", methods=['GET'])
def get():
    return jsonify({'gameresult': gameResults})


@gameScore.route("/gameResults/<int:id>", methods=['GET'])
def get_index(id):
    return jsonify({'gameresult': gameResults[id]})


@gameScore.route("/gameResults", methods=['POST'])
def create():
    # url = 'http://localhost:5000/gameResults'
    req_data = request.get_json()

    new_results = {
        'id': req_data['id'],
        'playerName': req_data['playerName'],
        'score': req_data['score'],
        'date': req_data['date']
    }
    gameResults.append(new_results)
    return jsonify(new_results)
    #return jsonify({'gameresult': gameResults[new_results]})


if __name__ == "__main__":
    gameScore.run(host='0.0.0.0', port = 5000, debug=True)
