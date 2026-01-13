"""
===========================================
FICHIER: ui/fenetre_principale.py
Interface graphique principale
===========================================
"""

from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit, QTableWidget,
                             QTableWidgetItem, QLabel, QMessageBox)
from PyQt6.QtCore import Qt
from database import (CreerBDD, InsererPoste, ModifierPoste, SupprimerPoste,
                      RecupererTousLesPostes, RechercherPostes)


class FenetrePrincipale(QWidget):
    """Fenêtre principale de l'application"""

    def __init__(self):
        super().__init__()
        self.selected_id = None
        self.initUI()
        self.afficher_tout()

    def initUI(self):
        """Initialiser l'interface utilisateur"""
        self.setWindowTitle("Gestion de Parc Informatique")
        self.setGeometry(100, 100, 1000, 650)

        # Titre
        self.titre = QLabel(self)
        self.titre.setText("GESTION DE PARC INFORMATIQUE")
        self.titre.setGeometry(35, 20, 930, 50)
        self.titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Section Recherche
        self.label_recherche = QLabel(self)
        self.label_recherche.setText("🔍 Recherche:")
        self.label_recherche.setGeometry(35, 90, 120, 30)

        self.line_edit_recherche = QLineEdit(self)
        self.line_edit_recherche.setGeometry(165, 90, 365, 35)
        self.line_edit_recherche.setPlaceholderText("Rechercher un poste...")
        self.line_edit_recherche.textChanged.connect(self.rechercher_poste)

        # Labels et champs de saisie
        labels_text = ["Nom Poste:", "Utilisateur:", "Système:", "Adresse IP:"]
        self.line_edits = []

        for i, label_text in enumerate(labels_text):
            # Label
            label = QLabel(self)
            label.setText(label_text)
            label.setGeometry(35, 145 + i * 50, 120, 30)

            # Champ de saisie
            line_edit = QLineEdit(self)
            line_edit.setGeometry(165, 145 + i * 50, 180, 35)
            self.line_edits.append(line_edit)

        # Boutons d'action
        btn_config = [
            ("➕ Ajouter", 370, 145, self.ajouter_poste),
            ("✏️ Modifier", 370, 195, self.modifier_poste),
            ("🗑️ Supprimer", 370, 245, self.supprimer_poste),
            ("🔄 Actualiser", 370, 295, self.afficher_tout),
            ("🗄️ Créer BDD", 530, 145, self.creer_bdd)
        ]

        for text, x, y, fonction in btn_config:
            btn = QPushButton(self)
            btn.setText(text)
            btn.setGeometry(x, y, 150, 40)
            btn.clicked.connect(fonction)

        # Tableau
        self.tableau = QTableWidget(self)
        self.tableau.setRowCount(0)
        self.tableau.setColumnCount(4)
        self.tableau.setGeometry(35, 360, 930, 260)
        self.tableau.setHorizontalHeaderLabels(['Nom Poste', 'Utilisateur', 'Système', 'Adresse IP'])
        self.tableau.cellClicked.connect(self.cellule_cliquee)

        # Ajuster largeur des colonnes
        self.tableau.setColumnWidth(0, 200)
        self.tableau.setColumnWidth(1, 200)
        self.tableau.setColumnWidth(2, 250)
        self.tableau.setColumnWidth(3, 250)

    def valider_adresse_ip(self, ip):
        """Valider le format d'une adresse IP"""
        parties = ip.split('.')
        if len(parties) != 4:
            return False

        for partie in parties:
            if not partie.isdigit():
                return False
            nombre = int(partie)
            if nombre < 0 or nombre > 255:
                return False

        return True

    def creer_bdd(self):
        """Créer/Réinitialiser la base de données"""
        reply = QMessageBox.question(
            self,
            'Confirmation',
            'Voulez-vous créer/réinitialiser la base de données?\n\n⚠️ Attention: Cela supprimera toutes les données existantes!',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            CreerBDD()
            QMessageBox.information(self, "Succès", "✅ Base de données créée avec succès!")
            self.afficher_tout()

    def ajouter_poste(self):
        """Ajouter un nouveau poste"""
        valeurs = [le.text() for le in self.line_edits]

        if not all(valeurs):
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs!")
            return

        # Validation de l'adresse IP
        adresse_ip = valeurs[3]
        if not self.valider_adresse_ip(adresse_ip):
            QMessageBox.warning(self, "Erreur", "L'adresse IP doit être au format 192.168.10.1")
            return

        InsererPoste(*valeurs)
        self.vider_champs()
        self.afficher_tout()

    def modifier_poste(self):
        """Modifier le poste sélectionné"""
        if not self.selected_id:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un poste à modifier!")
            return

        valeurs = [le.text() for le in self.line_edits]

        if not all(valeurs):
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs!")
            return

        # Validation de l'adresse IP
        adresse_ip = valeurs[3]
        if not self.valider_adresse_ip(adresse_ip):
            QMessageBox.warning(self, "Erreur", "L'adresse IP doit être au format 192.168.10.1")
            return

        ModifierPoste(self.selected_id, *valeurs)
        self.vider_champs()
        self.selected_id = None
        self.afficher_tout()

    def supprimer_poste(self):
        """Supprimer le poste sélectionné"""
        if not self.selected_id:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un poste à supprimer!")
            return

        SupprimerPoste(self.selected_id)
        self.selected_id = None
        self.afficher_tout()

    def rechercher_poste(self):
        """Rechercher des postes en temps réel"""
        terme = self.line_edit_recherche.text()

        if not terme:
            self.afficher_tout()
            return

        resultats = RechercherPostes(terme)
        self.remplir_tableau(resultats)

    def afficher_tout(self):
        """Afficher tous les postes"""
        self.vider_champs()
        self.line_edit_recherche.clear()
        self.selected_id = None
        resultats = RecupererTousLesPostes()
        self.remplir_tableau(resultats)

    def remplir_tableau(self, resultats):
        """Remplir le tableau avec des données"""
        self.tableau.setRowCount(len(resultats))

        for i in range(len(resultats)):
            for j in range(4):
                item = QTableWidgetItem(str(resultats[i][j + 1]))
                self.tableau.setItem(i, j, item)

    def cellule_cliquee(self, row, column):
        """Remplir les champs quand on clique sur une ligne"""
        resultats = RecupererTousLesPostes()
        if row < len(resultats):
            self.selected_id = resultats[row][0]

            for j in range(4):
                self.line_edits[j].setText(str(resultats[row][j + 1]))

    def vider_champs(self):
        """Vider tous les champs de saisie"""
        for le in self.line_edits:
            le.clear()