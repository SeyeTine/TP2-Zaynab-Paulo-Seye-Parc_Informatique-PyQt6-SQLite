# TP2-Zaynab-Paulo-Seye-Parc_Informatique-PyQt6-SQLite
420-2PR-BB TP2 Développement d’applications PyQt6 & SQLite

# Membres de l’équipe
Seye Tine – 6384223
Paulo Gualberto Correa Fernandes – 6334211
Zaynab Ahdadouch – 2321875

# Description
Cette application permet de gérer un parc informatique à l’aide d’une interface graphique développée en Python avec PyQt6, et d’une base de données SQLite.

# Similarité avec l’application Annuaire

Dans ce second projet, nous nous sommes inspirés de l’application Annuaire réalisée précédemment.
La structure générale du code a été conservée, mais celui-ci a été adapté à la gestion des postes de travail d’un parc informatique.

Cette approche nous a permis de réutiliser les concepts déjà maîtrisés tout en les appliquant à un nouveau contexte.

# Ajout de styles CSS (QSS)

Des styles CSS ont été ajoutés à l’application afin d’améliorer son apparence visuelle.
Cela permet de rendre l’interface plus moderne, agréable à utiliser et plus intuitive pour l’utilisateur.

Ces styles ont été appliqués aux boutons, aux champs de saisie, aux tableaux et aux titres, en utilisant les notions vues en cours.

# Fonctionnalités
➕ Ajouter un poste informatique
✏️ Modifier les informations d’un poste existant
🗑️ Supprimer un poste avec confirmation
🔍 Rechercher des postes en temps réel
🔄 Actualiser l’affichage
📊 Afficher tous les postes dans un tableau interactif

# Outils utilisées
Python
PyQt6 – Framework d’interface graphique
SQLite3 – Base de données légère intégrée

# Gestion du projet (GitHub & PyCharm)
Création du répertoire GitHub
Ajout des membres de l’équipe
Mise en place d’un tableau Kanban pour la gestion des tâches
Clonage du projet sur PyCharm
Création des issues et des branches associées
Développement du code sur chaque branche par la personne désignée
Commit régulier après chaque modification
Pull Request et merge vers la branche main

# Structure du projet

<img width="992" height="152" alt="image" src="https://github.com/user-attachments/assets/82de2dc4-3d28-4f09-8001-937e3d678968" />

# Captures d’écran et tests des fonctionnalités
▶️ Lancement de l’application
Lors du lancement de l’application, l’interface principale s’affiche correctement avec le tableau des postes.

➕ Ajouter un poste

Lors de l’ajout d’un poste, tous les champs doivent être remplis.
Si un champ est vide, un message d’erreur s’affiche et l’ajout est refusé.

Cette fonctionnalité permet d’assurer l’intégrité des données enregistrées dans la base de données.

✏️ Modifier un poste

Cette action montre que la fonctionnalité de modification fonctionne correctement.
Par exemple, le poste numéro 1 a été modifié avec succès et ses informations ont été mises à jour dans l’interface ainsi que dans la base de données.

🗑️ Supprimer un poste

Un poste a été ajouté volontairement uniquement dans le but de tester la fonctionnalité de suppression.
Cela confirme que la suppression fonctionne correctement et que les données sont bien retirées de la base de données.

🔍 Rechercher un poste

Dans ce projet, nous avons un nombre limité de postes.
Cependant, dans un véritable parc informatique, le nombre de postes peut être très élevé.
Nous avons donc jugé nécessaire d’ajouter une fonctionnalité de recherche afin de faciliter et d’accélérer la recherche d’un poste.

🗄️ Vérification de la base de données

Cette capture montre que la base de données parc_informatique.db a été correctement créée et connectée à l’application graphique.
Toutes les actions effectuées via l’interface (ajout, modification, suppression) sont automatiquement enregistrées dans la base de données.

✅ Conclusion
Ce projet nous a permis de mettre en pratique le développement d’une application graphique complète en PyQt6, connectée à une base de données SQLite, tout en appliquant les principes CRUD et une bonne organisation du code.
