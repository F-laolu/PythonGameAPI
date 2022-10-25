# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
from asyncio import constants
import json
from random import randint
from flask import Flask, jsonify, request
import azure.cosmos.cosmos_client as cosmos_client

import os

gameScore = Flask(__name__)


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
    gameResults = []

    results = container.query_items('SELECT * FROM c', enable_cross_partition_query=True)
    for doc in results:
        print (doc)
        gameResult = {
           'id': doc['id'], 'playerName': doc['playerName'], 'score': doc['score'], 'date': doc['date'] 
        }
        gameResults.append(gameResult)
    return jsonify({'gameresult': gameResults})
       
        
        

@gameScore.route("/gameResults/<int:id>", methods=['GET'])
def get_index(id):
    
    gameResults = []

    games = container.query_items('SELECT * FROM c', enable_cross_partition_query=True)
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
    document_id = container.create_item(new_results, populate_query_metrics=True)
    return str(document_id)
   
if __name__ == "__main__":

    config = {
        
            'ENDPOINT': 'https://olacosmosdbacc2.documents.azure.com:443/',
            'PRIMARYKEY': os.getenv('OlaDBconnkey2'),
            'DATABASE': 'GameDetails1',
            'CONTAINER': 'GameScores1'
        }
        
        # Initialize the Cosmos client
    client = cosmos_client.CosmosClient(url=config['ENDPOINT'], credential={'masterKey': config['PRIMARYKEY']})

    db = client.get_database_client(config['DATABASE'])
    container = db.get_container_client(config['CONTAINER'])
    
    gameScore.run(host='0.0.0.0', port = 5000, debug=True)
 