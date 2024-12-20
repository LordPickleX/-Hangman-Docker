from flask import Flask, render_template, request, session, jsonify, redirect
import requests  # Utilisation de requests pour envoyer des requêtes HTTP

app = Flask(__name__)

# Initialisation de l'application Flask
app.secret_key = "secret_key_for_session"  # Clé secrète pour sécuriser les sessions

@app.route("/", methods=["GET"])
def redirect_to_menu():
    return redirect("/menu")

@app.route("/menu", methods=["GET"])
def menu():
    return render_template("menu.html")

@app.route("/settings", methods=["GET"])
def settings():
    try:
        # Faire une requête au backend pour récupérer tous les mots
        response = requests.get("http://backend:2001/get_words")
        if response.status_code == 200:
            words = response.json().get("words", [])
        else:
            words = []
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des mots : {e}")
        words = []

    return render_template("settings.html", words=words)





@app.route("/game", methods=["GET"])
def home():
    # Vérifier si le mot est déjà dans la session
    if "mot" not in session:
        url = "http://backend:2001/get_random_word"  # Utiliser le nom du service "backend" pour accéder à l'API

        try:
            # Envoi de la requête GET pour récupérer le mot aléatoire
            print(f"Requête GET vers l'URL : {url}")
            response = requests.get(url)  # Utilisation de requests pour la requête GET

            # Vérifier que la réponse est correcte
            if response.status_code == 200:
                print(f"Réponse de l'API : {response.text}")
                data = response.json()  # Charger la réponse JSON
                mot_aleatoire = data.get("word", "chocolat")  # Mot par défaut si la clé "word" est absente
                print(f"Mot aléatoire récupéré : {mot_aleatoire}")
            else:
                print(f"Erreur dans la réponse de l'API, code de statut {response.status_code}")
                mot_aleatoire = "chocolat"  # Mot par défaut si la requête échoue
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête : {e}")
            mot_aleatoire = "chocolat"  # Mot par défaut en cas d'erreur

        # Initialiser la session avec le mot aléatoire
        session["mot"] = mot_aleatoire
        print(f"Mot stocké dans la session : {session['mot']}")
        session["guessed_letters"] = ["_" for _ in mot_aleatoire]  # Liste de tirets pour chaque lettre du mot
        session["health"] = 7  # Nombre de tentatives restantes
        session["lettre_perdues"] = []  # Liste des lettres perdues

    # Rendu du template avec les informations du jeu
    return render_template("index.html", mot=" ".join(session["guessed_letters"]), health=session["health"])








@app.route("/deviner", methods=["POST"])
def deviner():
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

    session["guessed_letters"] = guessed_letters
    session.modified = True

    mot_trouve = "_" not in guessed_letters
    perdu = session["health"] <= 0

    return jsonify({
        "mot": " ".join(guessed_letters),
        "health": session["health"],
        "mot_trouve": mot_trouve,
        "perdu": perdu,
        "mot_complet": mot if perdu else None,
        "lettre_perdu": lettres_perdues
    })

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return jsonify({"message": "Session réinitialisée avec succès."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2323)