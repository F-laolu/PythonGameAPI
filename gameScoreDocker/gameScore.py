# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

from asyncio.windows_events import NULL
import json

import getpass
from typing import Collection
import pymongo

from random import randint
from flask import Flask, jsonify, request

gameScore = Flask(__name__)

CONNECTION_STRING = 'mongodb://pythonapi-cosmos:9FSKdBpq9XY3SZg1DmegfgJYWp1ekf3RAp8hQs7Bq3dhs5v5RtDhkloDHed6AXb193Y5bu20dG3RvBTkBK44rg==@pythonapi-cosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@pythonapi-cosmos@' 
DB_NAME = "pythongame"
UNSHARDED_COLLECTION_NAME = "gameResult"
SAMPLE_FIELD_NAME = "sample_field"

#gameResults = [
    #{'id': "0", 'playerName': "Femi", 'score': "170", 'date': "08/02/2021"},
    #{'id': "1", 'playerName': "Ola", 'score': "90", 'date': "22/06/2021"},
    #{'id': "2", 'playerName': "Tola", 'score': "150", 'date': "22/07/2021"},
    #{'id': "3", 'playerName': "Wale", 'score': "160", 'date': "08/12/2021"},
#]


@gameScore.route('/')
def index():
    return "These are the game results data for various players, updated with github!!."

@gameScore.route("/gameResults", methods=['GET'])
def get():
    game = collection.find()
    gameResults = []
    for doc in game:
        print (doc)
        gameResult = {
           'id': doc['id'], 'playerName': doc['playerName'], 'score': doc['score'], 'date': doc['date'] 
        }
        gameResults.append(gameResult)
    return jsonify({'gameresult': gameResults})

@gameScore.route("/gameResults/<int:id>", methods=['GET'])
def get_index(id):
    games = collection.find()
    gameResults = []
    for doc in games:
        print (doc)
        gameResult = {
           'id': doc['id'], 'playerName': doc['playerName'], 'score': doc['score'], 'date': doc['date'] 
        }
        gameResults.append(gameResult)
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
    document_id = collection.insert_one(new_results).inserted_id
    return str(document_id)
   
if __name__ == "__main__":
    client = pymongo.MongoClient(CONNECTION_STRING)
    try:
        client.server_info() # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")

    collection = client[DB_NAME][UNSHARDED_COLLECTION_NAME]
    print (collection)
    gameScore.run(host='0.0.0.0', port = 5000, debug=True)
