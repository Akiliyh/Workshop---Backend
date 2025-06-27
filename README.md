# 🌐🔥 Linguicountry
*Imagine the lingui to your country*

- [🌐🔥 Linguicountry](#-linguicountry)
  - [📜 Description du projet](#-description-du-projet)
  - [⚖️ Organisation de l'équipe](#️-organisation-de-léquipe)
    - [🐜 Tâches à réaliser](#-tâches-à-réaliser)
      - [Modèle : Base de données](#modèle--base-de-données)
      - [Vue : HTML](#vue--html)
      - [Contrôleur : Flask](#contrôleur--flask)
      - [Général](#général)
    - [🐾 Répartition](#-répartition)
      - [🐿️ Guillaume](#️-guillaume)
      - [🐁 Lison](#-lison)
      - [🦐 Océane](#-océane)
  - [📨 Le Rendu](#-le-rendu)
    - [📝 Modèle Conceptuel des Données](#-modèle-conceptuel-des-données)
    - [💬 API REST](#-api-rest)
    - [🖥 Model - Vue - Controller](#-model---vue---controller)
  - [🗓️ Planning](#️-planning)
    - [1️⃣ Jour 1 - Lundi 23/06/2025](#1️⃣-jour-1---lundi-23062025)
    - [2️⃣ Jour 2 - Mardi 24/06/2025](#2️⃣-jour-2---mardi-24062025)
    - [3️⃣ Jour 3 - Mercredi 25/06/2025](#3️⃣-jour-3---mercredi-25062025)
    - [4️⃣ Jour 4 - Jeudi 26/06/2025](#4️⃣-jour-4---jeudi-26062025)
    - [5️⃣ Jour 5 - Vendredi 27/06/2025](#5️⃣-jour-5---vendredi-27062025)

## 📜 Description du projet
Ce projet<!-- a été réalisé --> est en cours de réalisation par Guillaume Boucher, Océane Drapeau et Lison Marvin. Il a <!-- eu -->lieu dans le cadre du workshop *Programmation Web S2* en IMAC1 dirigé par Sylvain Cherrier.
Le projet prend la forme d'un jeu style godgame où l'utilisateur crée et détruit des langages et pays suite à une apocalypse. Il n'y a plus que 10 000 habitants restants où il doit les placer au sein de différentes cultures et pays.

## ⚖️ Organisation de l'équipe

Nous échangeons sur GIT nos implémentations et résolvons nos différends par discussion en cours ou sur Discord.

La création du projet et le choix du thème a été choisi collectivement. Ensuite, nous avons déterminé ce qu'il fallait faire pour se répartir les tâches en fonction du schéma Model View Controller.

### 🐜 Tâches à réaliser

#### Modèle : Base de données
- [x] Réalisation d'un MCD
- [x] Création de la base de données
- [x] Création tables selon le MCD
- [ ] Ajout valeurs dans chaque table
- [x] Création [model.py](./model.py)
- [ ] Définition demandes à la base de données (create, insert, select, delete)
- [ ] Gestion initialisation (def init() → insert into)
- [ ] Gestion récupération des données pour l'affichage(def get() → select)
  
#### Vue : HTML
- [x] Création des pages de formulaires (pays, langue, point d'intérêt)
- [x] Création de la page d'accueil
- [x] Création des pages "fiches" (pays, langue, point d'intérêt)
  
#### Contrôleur : Flask
- [x] Création de [server.py](./server.py)
- [x] Création routes cohérentes
- [x] Récupération données de formulaires
- [x] Liaisons actions utilisateur (get, post, put, delete) aux actions BDD (create, insert, select, delete)

#### Général
- [x] Définition potentielles incohérences
- [ ] Gestion incohérences (python, JS)
- [x] Définition architecture du site

### 🐾 Répartition

#### 🐿️ Guillaume
- [x] Model : def get()
- [x] Model : def init()
- [x] Model : Connexion BDD-Flask
- [x] Vue : Amélioration accueil
- [x] Controller : routes
- [x] API : échange JSON
- [x] API : implémentation model vers api
  
#### 🐁 Lison
- [x] Model : def add()
- [x] Model : def delete()
- [x] Vue : formulaires
- [x] Vue : mise en forme CSS
- [x] Vue : fiches
- [x] Vue : accueil
- [x] Controller : routes

#### 🦐 Océane
- [ ] Model : def update()
- [x] Model : Ajout tables
- [x] Vue : Amélioration fiches
- [x] général : README
- [ ] API : implémentation model vers api
- [x] Général : Merges
- [x] Général : Uniformisation du code

## 📨 Le Rendu

### 📝 Modèle Conceptuel des Données

La première étape de notre travail fut de créer un MCD afin de correctement visualiser les informations et leur rangement. 
![Modèle Conceptuel des Données](/static/image(readme)/mcd.jpg)
Nous avons donc six tables dont une association plusieurs à plusieurs.
Ce schéma permet d'avoir trois tables princiaples : ```Countries```, ```Languages``` et ```InterestPoints```. Les tables ```WordOrder``` et ```TypePOI``` sont des informations supplémentaires tandis que l'association ```Countries_has_Languages``` permet de relier la table ```Countries``` et la table ```Languages``` tout en conservant des informations supplémentaires

### 💬 API REST

Nous utilisons l'API REST pour faire les requêtes à la base de données. Toutes les fonctions utilisant les méthodes PUT, GET, POST ou DELETE sont rangées dans le fichier ```api.py```. Voici une images de quelques unes de ces fonctions :
![capture d'écran du fichier api](/static/image(readme)/REST.jpg)
<sup>*(Attention l'image provient d'une ancienne version, le code s'y trouvant peut avoir changé depuis)*</sup>

### 🖥 Model - Vue - Controller

Nous avons séparé les différents composants en plusieurs fichers. En effet le Model se trouve dans le fichier ```model.py``` tandis que le Controller se répartit dans les fichiers ```api.py```qui regroupe les fonctions d'API REST et ```server.py```. Vue, quant à lui, correspond au dossier templates et static où se trouvent les fichiers HTML et CSS ainsi que JS. 
<img src="/static/image(readme)/MVC.jpeg" alt="capture d'écran de l'organisations des dossiers" width="30%">





## 🗓️ Planning

Nous gardons une trace de ce qu'il reste à faire par jour pour atteindre les rendus intermédiaires. Ceux-ci étant partagés en 3 : le MVP (minimum viable product) le 24/06 au soir, la V1 le 26/06 au soir et la version finale.

| Jour        | Grandes étapes  |
| ----------- | --------------- |
| 23/06       | Début du projet |
| 24/06 - MVP | Rendu du MVP    |
| 25/06       | Améliorations   |
| 26/06 - V1  | Rendu de la V1  |
| 27/06       | Soutenance      |

### 1️⃣ Jour 1 - Lundi 23/06/2025
- [x] Trouver une idée
- [x] Création BDD
- [x] Définition BDD
- [x] MCD (modèle conceptuel de données)
- [x] Planning prévisionnel

### 2️⃣ Jour 2 - Mardi 24/06/2025
- [x] Fix BDD
- [x] Routes
- [x] Finir tâches organisation
- [x] Créer les fichiers .py (MVP)
- [x] Créer templates

### 3️⃣ Jour 3 - Mercredi 25/06/2025
- [x] API REST
- [x] Amélioration formulaires
- [x] Avancer front
- [x] Commencer CSS
  
### 4️⃣ Jour 4 - Jeudi 26/06/2025
- [x] Finir le update
- [x] Faire les modals (pop up)
- [x] Redirect après les actions (add, modify)
- [x] Continuer le CSS
- [x] Injecter données en javascript

### 5️⃣ Jour 5 - Vendredi 27/06/2025

- [x] Résoudre le update sur language et country
- [x] Redirect du formulaire en JS
- [x] Résolution de problèmes divers
- [x] Présentation 
- [x] Finalisation du README
  




