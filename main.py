# Point d'entrée de l'application

from PyQt6.QtWidgets import QApplication
import sys
from ui import FenetrePrincipale
from database import CreerTable

def main():
    """Point d'entrée principal de l'application"""
    app = QApplication(sys.argv)

    # Créer la base de données au démarrage
    CreerTable()

    # Créer et afficher la fenêtre principale
    fenetre = FenetrePrincipale()
    fenetre.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()