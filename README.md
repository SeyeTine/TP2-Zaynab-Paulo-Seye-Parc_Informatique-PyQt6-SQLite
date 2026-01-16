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

# Fonctionnalités
➕ Ajouter un poste informatique
✏️ Modifier les informations d’un poste existant
🗑️ Supprimer un poste avec confirmation
🔍 Rechercher des postes en temps réel
🔄 Actualiser l’affichage

# Outils utilisées
Python - Language de programmation 
PyQt6 - Framework d'interface graphique
SQLite3 - Base de données intégrée

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

<img width="1230" height="832" alt="image" src="https://github.com/user-attachments/assets/83e5ccd7-dd5b-43c9-8ee1-8708eb266653" />

➕ Ajouter un poste

Lors de l’ajout d’un poste, tous les champs doivent être remplis.
Si un champ est vide, un message d’erreur s’affiche et l’ajout est refusé.
Cette fonctionnalité permet d’assurer l’intégrité des données enregistrées dans la base de données.
Une condition a également été ajoutée concernant le format de l’adresse IP.

<img width="1227" height="821" alt="image" src="https://github.com/user-attachments/assets/39805b4e-13d7-466c-b483-cc708c0d4f23" />

<img width="1227" height="821" alt="image" src="https://github.com/user-attachments/assets/27c60295-39e0-421c-84b1-17b9950ba7e1" />

Sur la capture en dessous, nous avons ajouté 3 postes de travail

<img width="1232" height="822" alt="image" src="https://github.com/user-attachments/assets/74c22de8-7626-466f-9a51-41f5d7f03749" />

✏️ Modifier un poste

Cette action montre que la fonctionnalité de modification fonctionne correctement.

<img width="1215" height="825" alt="image" src="https://github.com/user-attachments/assets/075ec621-7a0b-4070-8d8c-05fc19c72f00" />

Le system du PC de seye a été modifié. il passe de Windows a Windows 10 Pro

<img width="1231" height="816" alt="image" src="https://github.com/user-attachments/assets/e768944d-dc31-417e-a0c9-f8656a1620c4" />

🗑️ Supprimer un poste

Un poste a été ajouté volontairement uniquement dans le but de tester la fonctionnalité de suppression.

<img width="1210" height="815" alt="image" src="https://github.com/user-attachments/assets/ec1c6b7b-cd44-4914-ad6f-d52aaee6be21" />

Cela confirme que la suppression fonctionne correctement et que les données sont bien retirées de la base de données.

<img width="1207" height="817" alt="image" src="https://github.com/user-attachments/assets/ac67b0c7-fbc8-41c7-9514-38c93cd41250" />

🔍 Rechercher un poste

Dans ce projet, nous avons un nombre limité de postes.
Cependant, dans un véritable parc informatique, le nombre de postes peut être très élevé.
Nous avons donc jugé nécessaire d’ajouter une fonctionnalité de recherche afin de faciliter et d’accélérer la recherche d’un poste.

<img width="1232" height="813" alt="image" src="https://github.com/user-attachments/assets/9e53d73c-5e8d-49ce-81e8-a0d581cb387e" />

🗄️ Vérification de la base de données

Cette capture montre que la base de données parc_informatique.db a été correctement créée et connectée à l’application graphique.
Toutes les actions effectuées via l’interface (ajout, modification, suppression) sont automatiquement enregistrées dans la base de données.

Avant modification poste de Seye

<img width="976" height="187" alt="image" src="https://github.com/user-attachments/assets/6731688d-b728-43ac-994c-1509cc0f4fe5" />

Apres modification poste de Seye

<img width="986" height="182" alt="image" src="https://github.com/user-attachments/assets/264068c8-20ea-4803-b197-f965ff4db990" />

# Conclusion
Ce projet nous a permis de mettre en pratique le développement d’une application graphique complète en PyQt6, connectée à une base de données SQLite, tout en appliquant les principes CRUD et une bonne organisation du code.
