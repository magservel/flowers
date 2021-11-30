Objectif:
Construire une application Angular qui intéragit avec un modèle de Deep Learning. L'application doit permettre les choses suivantes:
- Via une page d'accueil, pouvoir utiliser le modèle pour prédire une nouvelle donnée
- Via une page d'ajout avec un formulaire, ajouter des données à un dataset
- Via une page de listing, lister les données présentes dans le dataset et lancer l'entraînement du modèle sur ces données

Le but n'est pas du tout d'avoir un modèle performant mais plutôt de mettre en place l'architecture pour communiquer avec lui.
Le choix du type de données et du problème de Machine Learning est totalement libre, le cas le plus simple sera donc sûrement une régression univariée (e.g. prédire le prix d'une maison étant donné sa superficie). A nouveau, les performances du modèle et l'intérêt du problème n'ont aucune importance dans l'exercice, vous n'êtes donc pas obligé d'y passer du temps. De plus, les données peuvent être totalement fausses (pas la peine d'aller chercher un dataset en ligne).
Dans les étapes suivante, on considèrera une donnée (ou un exemple) comme une paire <x,y> avec y le label à prédire pour le modèle étant donné l'entrée x.

Vous êtes également libre sur vos choix d'architecture de code, convention de nommage et choix visuels (pas besoin de s'embêter beaucoup de CSS, un peu de Boostrap peut être une bonne idée).
Les bonus ne sont pas obligatoires. Si vous pensez pouvoir les faire rapidement (par exemple si vous l'avez déjà fait par le passé), n'hésitez-pas :)


Etapes:
1. Créer une API REST avec Flask
   1. Ajouter une base de données (pas besoin de quelque chose de compliqué, quelque chose in-memory comme https://pypi.org/project/tinydb/ suffit largement).
   2. Créer une route (route d'ajout) qui ajoute un exemple (paire <x,y>) dans la base.
   3. Créer une route (route de listing) qui liste les exemples présents dans la base.
   4. Créer une route (route d'entraînement) qui permettra de lancer un entraînement.
   5. Créer une route (route d'inférence) qui permettra d'utiliser le modèle pour prédire étant donné une entrée (la route recevra x et devra renvoyer y). 
2. Créer une application Angular >= 12
   1. Créer un service permettant de communiquer avec les routes de l'API REST Flask.
   2. Créer une page d'accueil avec un formulaire pour entrer x et appeler la route d'inférence. Le résultat (y) sera ensuite affiché.
   3. Créer une page avec un formulaire pour entrer x et y et les ajouter à la base (route d'ajout).
   4. Créer une page qui permet de lister les exemples dans la base (route de listing).
   5. Ajouter un bouton qui appelle l'entraînement du modèle (route d'entraînement) sur la précédente page.
3. Créer le modèle
   1. Créer un réseau de neurones (l'architecture n'a pas d'importance, un réseau feedforward est suffisant) en Python (e.g. Tensorflow, Keras, PyTorch).
   2. L'initialiser au démarrage de l'API REST Flask.
   3. Faire en sorte que la route d'inférence appelle le modèle avec le x donné et renvoie le retour du modèle (y).
   4. Faire en sorte que la route d'entraînement construise un jeu de données à partir de la base et entraîne le modèle avec. Aucune importance si le modèle est réinitialisé avant d'être entraîné ou s'il est appris online.


Bonus:
1. Découper le dataset en train/test avant de lancer l'entraînement et afficher les performances sur le test set dans l'application
2. Mettre en place un tensorboard pour monitorer l'entraînement
3. Faire des checkpoints du modèle et les recharger au démarrage de l'API