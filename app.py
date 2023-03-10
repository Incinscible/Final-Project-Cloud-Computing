from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
# import load_ligue1_teams

app = Flask(__name__, static_folder='templates')

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://db:27017/')
db = client['football']

@app.route('/')
def index():
    # Récupération de toutes les équipes de football
    teams = db.teams.find()
    return render_template('index.html', teams=teams)

@app.route('/caca', methods=['GET'])
def YOlegang():
    return "LA MALA EST GANGX"

@app.route('/team', methods=['POST'])
def team_players():
    # Récupération du nom de l'équipe à partir du corps de la requête
    teamName = request.json['teamName']

    # Récupération de l'effectif de l'équipe de football
    team = db.teams.find_one({'name': teamName})
    players = team['players']
    return jsonify(players)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)