# Fichier : app.py

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Route pour la page d'accueil ("/")
@app.get("/")
def home():
    prenom = "Alex"
    cours = ["Flask", "Jinja", "HTTP"]
    aujourdhui = datetime.now()
    return render_template("hello.html",
                           prenom=prenom,
                           cours=cours,
                           aujourdhui=aujourdhui)

# Route pour la page de bonjour personnalisée ("/bonjour/<nom>")
@app.get("/bonjour/<nom>")
def bonjour(nom):
    return render_template("hello.html",
                           prenom=nom,
                           cours=["Flask"],
                           aujourdhui=None)

# Lancement de l'application en mode debug
if __name__ == "__main__":
    app.run(debug=True)