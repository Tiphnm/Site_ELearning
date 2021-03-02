# Site E_Learning 

### Objectifs du brief

Réaliser un projet mini full stack, travailler en collaboration

### Langages 

Python, MYSQL, Flask, HTML, CSS, GitHub, Figma

### Descriptif du projet 

Réalisation d'un site pour apprendre le code via des tutorials videos. 
Création d'une base de donnée MYSQL, remplie grâce à des inputs users sur nos pages créer en HTML et CSS.
Notre database est composée d'une table contentant un id, la catégorie à laquelle appartient la vidéo, son titre et son lien.
Notre site est composée: d'une page d'accueil, de pages consacrées aux vidéos Python, Javascript et Azure.

### Architecture du projet 

- db.py : Contient la connection avec la base de données
- api.py : Contient les éléments permettant de faire une API avec flask
- /templates & /Static : Contient les fichiers HTML & CSS créer a partir du template Jinja inclus dans flask
- DockerFile, DockerCompose & wait-for-it.sh : Fichier permettant de dockeriser le projet

Maxime Chagnon 
Tiphaine Minguet 
Rachid Boubaya 
