from flask import Flask, render_template, request, session, jsonify, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuration de la base de données
db_config = {
    'host': 'mysql',  # Nom du service ou de l'hôte
    'user': 'admin',  # Nom d'utilisateur
    'password': 'death',  # Mot de passe
    'database': 'words_dictionary'  # Nom de la base de données
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as err:
        print(f"Erreur de connexion à la base de données: {err}")
        return None

@app.route("/", methods=["GET"])
def redirect_to_menu():
    return redirect("/get_random_word")


@app.route("/get_random_word", methods=["GET"])
def get_random_word():
    try:
        db = get_db_connection()
        if db is None:
            return jsonify({"word": "chocolat", "error": "Impossible de se connecter à la base de données."})

        cursor = db.cursor()
        cursor.execute("SELECT word FROM words_dictionary ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        cursor.close()
        db.close()

        word = result[0] if result else "chocolat"
        return jsonify({"word": word})

    except Error as err:
        print(f"Database error: {err}")
        return jsonify({"word": "chocolat", "error": "Une erreur est survenue"})


@app.route("/get_words", methods=["GET"])
def get_words():
    try:
        db = get_db_connection()
        if db is None:
            return jsonify({"error": "Impossible de se connecter à la base de données"}), 500

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM words_dictionary")
        words = cursor.fetchall()
        cursor.close()
        db.close()

        return jsonify({"words": words}), 200
    except Error as err:
        print(f"Erreur de base de données : {err}")
        return jsonify({"error": "Une erreur est survenue"}), 500


@app.route("/add_word", methods=["POST"])
def add_word():
    try:
        data = request.get_json()
        new_word = data.get("word", "").strip()

        if not new_word:
            return jsonify({"error": "Le mot est vide ou invalide"}), 400

        db = get_db_connection()
        if db is None:
            return jsonify({"error": "Impossible de se connecter à la base de données"}), 500

        cursor = db.cursor()
        cursor.execute("INSERT INTO words_dictionary (word) VALUES (%s)", (new_word,))
        db.commit()
        cursor.close()
        db.close()

        return jsonify({"message": "Mot ajouté avec succès", "word": new_word}), 201

    except Error as err:
        print(f"Erreur de base de données : {err}")
        return jsonify({"error": "Une erreur est survenue"}), 500


@app.route("/delete_word/<int:word_id>", methods=["DELETE"])
def delete_word(word_id):
    try:
        db = get_db_connection()
        if db is None:
            return jsonify({"error": "Impossible de se connecter à la base de données"}), 500

        cursor = db.cursor()
        cursor.execute("DELETE FROM words_dictionary WHERE id = %s", (word_id,))
        db.commit()

        if cursor.rowcount == 0:
            cursor.close()
            db.close()
            return jsonify({"error": "Mot introuvable"}), 404

        cursor.close()
        db.close()
        return jsonify({"message": "Mot supprimé avec succès"}), 200

    except Error as err:
        print(f"Erreur de base de données : {err}")
        return jsonify({"error": "Une erreur est survenue"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2001)