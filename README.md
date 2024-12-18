# -Hangman-Docker
Hangman game web-app using Docker for deployment and using a modular architectur as flask to manage application
and Node.js for the request the db

This application is a digital version of the Hangman game, where players guess letters to uncover a hidden word.

# How It Works

## Application Architecture
1. Frontend (HTML/JavaScript):
Interacts with Flask through HTTP requests to perform actions like guessing letters and resetting the game.
Optionally interacts directly with Node.js to fetch random words.
2. Flask (Python):
Handles the game logic (sessions, health, guessed letters, etc.).
Renders HTML pages and serves APIs for frontend interaction.
Requests words from Node.js when initializing the game.
3. Node.js (Express):
Provides access to the MySQL database.
Exposes an endpoint (/get-word) to fetch random words.
4. SQL Database:
Stores words used in the game.

# How to Play

docker-compose up --build




## Tâches à faire Evan
1. **Élément 1** : écrire des requêtes SQL :
- liste des mots par catégorie
- obtenir un mot d'un catégorie
- ajouter un mot dans un catégorie
- supprimer un mot dans un catégorie

## Bibliothèque python a installer 

pip install 


