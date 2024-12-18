"""
le fichier python app gere tout le deroulement du jeu et le processus des pages webs

la bibliotheque qui permet ca c'est flask

"""

from flask import Flask, render_template, request, session, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy.dialects import mysql
from sqlalchemy import create_engine
import mysql.connector
from flask import session



# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = "secret_key_for_session"  # Clé secrète pour sécuriser les sessions

# Redirection vers le menu principal par défaut
@app.route("/", methods=["GET"])
# fonction qui redirige l'utilisateur vers la page menu
def redirect_to_menu():
    return redirect("/menu")

@app.route("/menu", methods=["GET"])
# fonction qui affiche la page html menu
def menu():
    return render_template("menu.html")

@app.route("/settings", methods=["GET"])
# fonction qui affiche la page html menu
def menu():
    return render_template("settings.html")










# Configuration de la base de données
db_config = {
    'host': 'mysql',  # Nom du service ou de l'hôte
    'user': 'admin',  # Nom d'utilisateur
    'password': 'death',  # Mot de passe
    'database': 'words_dictionary'  # Nom de la base de données
}








def get_random_word():
    try:
        # Initialisation de la connexion à la base de données
        db = mysql.connector.connect(**db_config)

        # Vérification de la connexion
        if db.is_connected():
            cursor = db.cursor()
            cursor.execute("SELECT word FROM words_dictionary ORDER BY RAND() LIMIT 1")
            result = cursor.fetchone()
            cursor.close()
            db.close()

            if result:
                return result[0]
            else:
                return "chocolat"  # Mot par défaut si aucun mot n'est trouvé
        else:
            return "chocolat"  # Mot par défaut si la connexion échoue

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return "chocolat"  # Mot par défaut en cas d'erreur



def add_word():
    try:
        # Initialisation de la connexion à la base de données
        db = mysql.connector.connect(**db_config)

        # Vérification de la connexion
        if db.is_connected():
            cursor = db.cursor()
            cursor.execute("SELECT word FROM words_dictionary ORDER BY RAND() LIMIT 1")
            cursor.execute("INSERT INTO words_dictionary()")
            #result = cursor.fetchone()
            cursor.close()
            db.close()
        else:
            return "chocolat"  # Mot par défaut si la connexion échoue

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        #return "chocolat"  # Mot par défaut en cas d'erreur







# Route pour afficher la page de jeu
@app.route("/game", methods=["GET"])
def home():
    # initialisation des données dans la session si elles n'existent pas encore
    # cela permet de ne pas le refaire a chaque fois qu'on fait une action
    if "mot" not in session:
        mot_aleatoire = get_random_word()
        session["mot"] = mot_aleatoire
        session["guessed_letters"] = ["_" for _ in session["mot"]]
        session["health"] = 7
        session["lettre_perdues"] = []

    # on passe les données nécessaires mot et santé
    # ce sont les variables qui seront dans le fichier html
    return render_template("index.html", mot=" ".join(session["guessed_letters"]), health=session["health"])



"""
# Route pour afficher la page de jeu
@app.route("/game", methods=["GET"])
def home():
    # initialisation des données dans la session si elles n'existent pas encore
    # cela permet de ne pas le refaire a chaque fois qu'on fait une action
    if "mot" not in session:
        # mot_aleatoire = get_random_word()
        session["mot"] = "chocolat"
        session["guessed_letters"] = ["_" for _ in session["mot"]]
        session["health"] = 7

    # on passe les données nécessaires mot et santé
    # ce sont les variables qui seront dans le fichier html
    return render_template("index.html", mot=" ".join(session["guessed_letters"]), health=session["health"])

"""




# Route pour gérer la logique de devinette
@app.route("/deviner", methods=["POST"])
def deviner():
    # Récupère la lettre envoyée depuis le client
    lettre = request.json.get("lettre", "").lower()
    if len(lettre) != 1 or not lettre.isalpha():
        return jsonify({"error": "Lettre invalide"}), 400

    guessed_letters = session["guessed_letters"]
    mot = session["mot"]
    lettres_perdues = session.get("lettre_perdues", [])


    if lettre in mot:
        for i, char in enumerate(mot):
            if char == lettre:
                guessed_letters[i] = lettre
    else:
        session["health"] -= 1
        lettres_perdues.append(lettre)

    print(lettres_perdues)

    session["guessed_letters"] = guessed_letters
    session.modified = True

    # vérifie si le jeu est gagné ou perdu
    mot_trouve = "_" not in guessed_letters  # le mot est trouvé si plus de "_"
    perdu = session["health"] <= 0  # le jeu est perdu si plus de vies

    # état actuel du jeu
    return jsonify({
        "mot": " ".join(guessed_letters),  # mot partiellement deviné
        "health": session["health"],  # vies restantes
        "mot_trouve": mot_trouve,  # indique si le mot est trouvé
        "perdu": perdu,  # indique si le jeu est perdu
        "mot_complet": mot if perdu else None,  # révèle le mot si perdu
        "lettre_perdu": lettres_perdues
    })

# Route pour réinitialiser le jeu
@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return jsonify({"message": "Session réinitialisée avec succès."})

if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0" , port=2323)
