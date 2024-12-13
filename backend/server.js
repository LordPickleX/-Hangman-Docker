// server.js
const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Configuration de la base de données
const db = mysql.createConnection({
  host: 'mysql', // Nom du service MySQL dans Docker Compose
  user: 'admin',
  password: 'death',
  database: 'words_dictionary', // Nom de la base de données définie dans Docker Compose
});

// Tester la connexion
db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// Route pour récupérer un mot pour le jeu Hangman
app.get('/get-word', (req, res) => {
  db.query('SELECT word FROM words_dictionary ORDER BY RAND() LIMIT 1', (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Error retrieving word from database' });
      return;
    }
    res.json(results[0]); // Envoie le mot récupéré
  });
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});