import pymongo
import requests

client = pymongo.MongoClient("mongodb://db:27017/")
db = client["football"]
teams_collection = db["teams"]

teams_data = [
    {
        "name": "Paris Saint-Germain",
        "players": ["K. Mbappé", "L. Messi", "Neymar", "Juan Bernat", "M. Verratti", "Fabián Ruiz", "N. Mukiele", "Danilo Pereira", "Marquinhos", "Sergio Ramos", "G. Donnarumma"]
    },
    {
        "name": "Olympique Lyonnais",
        "players": ["K. Toko Ekambi", "A. Lacazette", "Tetê", "M. Caqueret", "J. Lepenant", "R. Faivre", "N. Tagliafico", "C. Lukeba", "Thiago Mendes", "M. Gusto", "Anthony Lopes"]
    },
    {
        "name": "Lille OSC",
        "players": ["J. David", "J. Bamba", "R. Cabella", "A. Ounas", "A. Gomes", "B. André", "Ismaily", "Tiago Djaló", "José Fonte", "B. Diakité", "L. Chevalier"]
    },
    {
        "name": "AS Monaco",
        "players": ["W. Ben Yedder","E. Ben Seghir","A. Golovin", "K. Diatta","Mohamed Camara","Y. Fofana","Caio Henrique","G. Maripán","A. Disasi","Vanderson", "A. Nübel"]
    },
    {
        "name": "Olympique de Marseille",
        "players": ["A. Sánchez", "D. Payet", "C. Ünder", "Nuno Tavares", "J. Veretout", "V. Rongier", "J. Clauss", "L. Balerdi", "S. Gigot", "C. Mbemba", "Pau López"]
    },
    {
        "name": "Toulouse FC",
        "players": ["Rafael Ratão", "T. Dallinga", "Z. Aboukhlal","B. van den Boomen","S. Spierings","B. Dejaegere","I. Sylla","R. Nicolaisen","A. Rouault","M. Desler","M. Dupé"]
    },
    {
        "name": "Stade Rennais FC",
        "players": ["E. Camavinga", "G. Laborde", "M. Terrier", "M. Dembélé", "S. Guirassy", "S. N'Zonzi", "F. Maouassa", "B. Soppy", "D. Da Silva", "L. Baal", "A. Gomis"]
    },
    {
        "name": "AS Saint-Étienne",
        "players": ["W. Khazri", "D. Bouanga", "M. Abi", "Y. Neyou", "L. Gourna", "P. Gabard", "M. Trauco", "H. Moukoudi", "P. Retsos", "T. Kolodziejczak", "É. Green"]
    },
    {
        "name": "OGC Nice",
        "players": ["K. Dolberg", "A. Gouiri", "J. Reine-Adélaïde", "M. Schneiderlin", "H. Boudaoui", "J. Kluivert", "Y. Atal", "J. Lotomba", "J. Todibo", "W. Saliba", "T. Benitez"]
    },
    {
        "name": "FC Metz",
        "players": ["V. Angban", "F. Boulaya", "F. Centonze", "F. Lacroix", "D. Bronn", "B. Kouyaté", "V. Pajot", "V. Udol", "D. Fofana", "A. Oukidja", "M. Caillard"]
    },
    {
        "name": "Angers SCO",
        "players": ["A. Fulgini", "M. Pereira Lage","A. Hunou", "S. Bahoken", "I. Amadou", "A. Bamba", "A. Bobichon", "S. Doumbia", "K. Boma Ndende", "M. Pavlovic", "P. Bernardoni"]
    },
    {
        "name": "Stade Brestois 29",
        "players": ["G. Charbonnier", "Achraf Dari","R. Cardona", "I. Cardona", "H. Magnetti", "L. Perraud", "F. Honorat", "P. Lasne", "B. Belkebla", "C. Battocchio", "R. Faivre"]
    },
    {
        "name": "Girondins de Bordeaux",
        "players": ["Hwang Ui-jo", "S. Kalu","Aliou Badji", "R. Oudin", "T. Lacoux", "J. Seri", "E. Kwateng", "Pablo", "L. Benito", "L. Bessile", "G. Poussin"]
    },
    {
        "name": "Clermont Foot",
        "players": ["J. Berthomier", "A. Grbic", "Alidu Seidu","J. Allevinah", "A. Gastien", "V. N'Simba", "C. Hountondji", "F. Ogier", "F. Centonze", "J. Phojo", "M. Jeannin"]
    },
    {
        "name": "FC Lorient",
        "players": ["T. Moffi","Bamba Dieng", "Y. Wissa", "A. Gravillon", "E. Le Fée", "E. Mendes", "L. Abergel", "T. Monconduit", "V. Le Goff", "J. Laporte", "P. Nardi"]
    },
    {
        "name": "Montpellier HSC",
        "players": ["G. Laborde","Wahbi Khazri", "S. Mavididi", "S. Wahi", "J. Ferri", "T. Savanier", "N. Cozza", "H. Hilton", "Pedro Mendes", "D. Congré", "J. Omlin"]
    },
    {
        "name": "Nantes FC",
        "players": ["L. Blas","Andy Delort", "K. Coulibaly", "L. Evangelista", "R. Kolo Muani", "K. Bamba", "C. Louza", "P. Abeid", "A. Girotto", "C. Traoré", "A. Lafont"]
    },
    {
        "name": "Auxerre FC",
        "players": ["M. Niang", "M. Autret", "Y. M'Changama", "H. Sakhi","G. Hein", "B. Touré", "Q. Bernard", "A. Coeff", "Jubal", "P. Joly", "B. Costil"]
    },
    {
        "name": "AC Ajaccio",
        "players": ["R. Hamouma	", "M. El Idrissy", "Y. Belaïli", "M. Coutadeur", "V. Marchetti", "C. Bayala", "I. Diallo", "C. Avinel", "O. Gonzalez", "M. Youssouf", "B. Leroy"]
    },
    {
        "name": "Auxerre FC",
        "players": ["Mama Baldé", "W. Odobert", "F. Tardieu", "R. Kouamé", "Rony Lopes", "Y. Larouci", "T. Baldé", "Y. Salmier", "E. Palmer-Brown", "J. Porozo", "G. Gallon"]
    },

       
]

for team in teams_data:
    teams_collection.insert_one(team)