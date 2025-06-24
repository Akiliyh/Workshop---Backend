# 🌐🔥 Linguicountry
*Imagine the lingui to your country*

## 📜 Description du projet
Ce projet<!-- a été réalisé --> est en cours de réalisation par Guillaume Boucher, Océane Drapeau et Lison Marvin. Il a <!-- eu -->lieu dans le cadre du workshop *Programmation Web S2* en IMAC1 dirigé par Sylvain Cherrier.

## ⚖️ Organisation de l'équipe

Nous échangeons sur GIT nos implémentations et résolvons nos différends par discussion en cours ou sur Discord.

La création du projet et le choix du thème a été choisi collectivement. Ensuite, nous avons déterminé ce qu'il fallait faire pour se répartir les tâches en fonction du schéma Model View Controller.

### 🐜 Tâches à réaliser

#### Modèle : Base de données
- [x] Réalisation d'un MCD
- [x] Création de la base de données
- [x] Création tables selon le MCD
- [ ] Ajout valeurs dans chaque table
- [ ] Création [model.py](./model.py)
- [ ] Définition demandes à la base de données (create, insert, select, delete)
- [ ] Gestion initialisation (def init() → insert into)
- [ ] Gestion récupération des données pour l'affichage(def show() → select)
  
#### Vue : HTML
- [ ] Création des pages de formulaires (pays, langue, point d'intérêt)
- [ ] Création de la page d'accueil
- [ ] Création des pages "fiches" (pays, langue, point d'intérêt)
  
#### Contrôleur : Flask
- [x] Création de [server.py](./server.py)
- [x] Création routes cohérentes
- [ ] Récupération données de formulaires
- [ ] Liaisons actions utilisateur (get, post, put, delete) aux actions BDD (create, insert, select, delete)

#### Général
- [x] Définition potentielles incohérences
- [ ] Gestion incohérences (python, JS)
- [x] Définition architecture du site

### 🐾 Répartition

#### 🐿️ Guillaume
- [ ] Model : def update()
- [ ] Model : def init()
- [ ] Vue : accueil
- [ ] Controller : routes
  
#### 🐁 Lison
- [ ] Model : def add()
- [ ] Model : def delete()
- [ ] Vue : formulaires
- [ ] Controller : routes

#### 🦐 Océane
- [ ] Model : def show()
- [ ] Model : Ajout tables
- [ ] Vue : fiches


### 🗓️ Planning

Nous gardons une trace de ce qu'il reste à faire par jour pour atteindre les rendus intermédiaires. Ceux-ci étant partagés en 3 : le MVP (minimum viable product) le 24/06 au soir, la V1 le 26/06 au soir et la version finale.

| Jour        | Grandes étapes  |
| ----------- | --------------- |
| 23/06       | Début du projet |
| 24/06 - MVP | Rendu du MVP    |
| 25/06       | Améliorations   |
| 26/06 - V1  | Rendu de la V1  |
| 27/06       | Soutenance      |

### 1️⃣ Jour 1
<!-- 3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟 -->

### 2️⃣ Jour 2
- [ ] Fix BDD
- [ ] Routes
- [ ] Finir tâches organisation
- [ ] Créer fichiers.py (MVP)
- [ ] Créer templates



