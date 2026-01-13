# Gestion de la base de données

import sqlite3

def CreerTable():
    """Créer la table ParcInformatique si elle n'existe pas"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS ParcInformatique
                   (ID INTEGER PRIMARY KEY
                       AUTOINCREMENT,
                       NomPoste TEXT NOT ULL,
                       Utilisateur TEXT NOT NULL,
                       Systeme TEXT NOT NULL,
                       AdresseIP TEXT NOT NULL);
                   """)
    conn.commit()
    conn.close()

def CreerBDD():
    """Créer/Réinitialiser la base de données"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()

    # Supprimer la table si elle existe
    cursor.execute("DROP TABLE IF EXISTS ParcInformatique")

    # Recréer la table
    cursor.execute("""
                   CREATE TABLE ParcInformatique
                   (ID INTEGER PRIMARY KEY
                       AUTOINCREMENT,
                       NomPoste TEXT NOT ULL,
                       Utilisateur TEXT NOT NULL,
                       Systeme TEXT NOT NULL,
                       AdresseIP TEXT NOT NULL);
                   """)

    conn.commit()
    conn.close()

def InsererPoste(nom_poste, utilisateur, systeme, adresse_ip):
    """Ajouter un nouveau poste"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO ParcInformatique (NomPoste, Utilisateur, Systeme, AdresseIP)
                   VALUES (?, ?, ?, ?) """, (nom_poste, utilisateur, systeme, adresse_ip))

    conn.commit()
    conn.close()

def ModifierPoste(id_poste, nom_poste, utilisateur, systeme, adresse_ip):
    """Modifier un poste existant"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE ParcInformatique
                   SET NomPoste    = ?,
                       Utilisateur = ?,
                       Systeme     = ?,
                       AdresseIP   = ?
                   WHERE ID = ?
                   """, (nom_poste, utilisateur, systeme, adresse_ip, id_poste))

    conn.commit()
    conn.close()

def SupprimerPoste(id_poste):
    """Supprimer un poste"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ParcInformatique WHERE ID = ?", (id_poste,))
    conn.commit()
    conn.close()

def RecupererTousLesPostes():
    """Récupérer tous les postes"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ParcInformatique ORDER BY NomPoste")
    resultat = cursor.fetchall()
    conn.close()
    return resultat

def RechercherPostes(terme):
    """Rechercher des postes"""
    conn = sqlite3.connect("parc_informatique.db")
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT *
                   FROM ParcInformatique
                   WHERE NomPoste LIKE ?
                      OR Utilisateur LIKE ?
                      OR Systeme LIKE ?
                      OR AdresseIP LIKE ?
                   ORDER BY NomPoste
                   """, (f'%{terme}%', f'%{terme}%', f'%{terme}%', f'%{terme}%'))

    resultat = cursor.fetchall()
    conn.close()
    return resultat