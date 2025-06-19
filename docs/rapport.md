# Déployer et utiliser MongoDB

## MongoDB Standalone

> **tip :** Ce TP sera réalisé sur Windows.

### Installation

1. **Téléchargement :**  
   Téléchargez la version de MongoDB correspondant à votre système :

   ![Capture d'écran du téléchargement de MongoDB](image.png)

2. **Installation :**  
   Installez MongoDB sur votre machine :

   ![Processus d'installation de MongoDB](image-1.png)

3. **MongoDB Compass :**  
   Ce processus installe également MongoDB Compass, une interface graphique qui vous permettra de mieux visualiser et interagir avec vos bases de données :

   ![Interface de MongoDB Compass](image-2.png)
   ![Vue complémentaire de MongoDB Compass](image-3.png)

### Configuration de la connexion

Une fois l'installation terminée, suivez ces étapes :

1. **Ajout d'une connexion :**  
   Après l'installation, ajoutez une nouvelle connexion :

   ![Configuration de la connexion](image-4.png)

2. **Paramètres par défaut :**  
   Conservez les paramètres par défaut, car aucun ajustement n'est nécessaire à ce stade :

   ![Paramètres par défaut](image-5.png)

3. **Vérification :**  
   La connexion finalisée s'affiche comme suit :

   ![Vue finale de la connexion](image-6.png)

### Lancement du shell Mongosh

On va maintenant pouvoir lancer le shell soit dans un cmd en ecrivant

```bash
mongosh
```

soit sur Compass juste ici :
![alt text](image-7.png)

On va se placer dans la base admin :

![alt text](image-8.png)

### Creation de l'utilisateur

Puis créer un nouvel utilisateur que l'on appelera "Matthis" avec comme mot de passe "MotDePasseIndechiffrable".

On lui attribue ensuite le rôle readWrite sur la base testdb que l'on va créer juste après

![alt text](image-9.png)

### Création de la base testdb et insertion de documents

Maintenant pour créer la base, on va d'abord se déplacer dedans (même si elle n'existe pas)

![alt text](image-10.png)

puis on va insérer dans une collection nommée employes, un employé nommé kevin malone, et on a maintenant la base qui s'est créée:

![alt text](image-11.png)

On va rajouter quelques autres employés :
![alt text](image-12.png)

Et maintenant si on va voir dans la collection :

![alt text](image-13.png)

On a bien nos 3 documents employés

## Replica Set

### Preambule

Pour les replicaSet, on va avoir besoin de mongod accessible dans les variables d'environnement pour pouvoir l'appeler en cmd :
![alt text](image-14.png)

En suite dans le dossier replicaset on creé 3 dossier, un par instance : data1 data2 et data3

![alt text](image-15.png)

### Deploiement des Replica

On va ensuite ouvrir 3 terminal et se placer dans replicaset
![alt text](image-16.png)

Puis dans chaque terminal, on va deployer une instance avec les commande suivante :

```
mongod --replSet rs0 --port 27018 --dbpath ./data1 --bind_ip localhost --logpath ./data1/mongod.log --logappend

mongod --replSet rs0 --port 27019 --dbpath ./data2 --bind_ip localhost --logpath ./data2/mongod.log --logappend

mongod --replSet rs0 --port 27020 --dbpath ./data3 --bind_ip localhost --logpath ./data3/mongod.log --logappend
```

Ces commandes vont créer et executer nos replicats :

- la premiere dans data1 sur le port 27018
- la seconde dans data2 sur le port 27019
- la derniere dans data3 sur le port 27020

### initialisation du replicaset

On va se connecter a la premiere instance : celle en 27018 (mongosh --port 27018), et executer cette commande qui audra pour effet de definir nos 3 instances dans le replicaSet rs0 (je l'avais deja fait une fois mais j'ai perdu le screen c'est pour ça qu'il y a marqué already initialized):

![alt text](image-17.png)

maintenant verfions chaque instance :

- 27018 : ![alt text](image-18.png)

- 27019 : ![alt text](image-19.png)

- 27020 : ![alt text](image-20.png)

### insertion sur le primary

On va maintenant se connecter sur le primary et y rajouter un nouvel employé et voir si cela se repercute sur nos secondary

Sur 27018 (primary) :
![alt text](image-21.png)

maintenant on va se rendre sur 27019 et 27020 et faire un

```
db.employes.find()
```

pour récupérer notre employé :

Sur l'instance 27019 :

![alt text](image-22.png)

et sur 27020 :

![alt text](image-23.png)

On peut donc en conclure que la réplication a marché.

## Integration

Nous avons créer un script python simple utilisant la librairie pymongo et  qui va se connecter a la base standalone avec le compte admin créer précédemment(27017), puis qui va dans un premier temps :

Insertion :
Le script insère un document "comptabilité" dans une nouvelle collection "services"

![alt text](image-24.png)


Lecture :
Il recherche et affiche ensuite les documents ayant le champ name égal à "Comptabilité" afin de confirmer que l'insertion a bien eu lieu.

![alt text](image-25.png)

Mise à jour :
Le document est modifié : la valeur du champ name passe de "Comptabilité" à "IT".

![alt text](image-26.png)

Suppression :
Enfin, le document mis à jour (celui avec name égal à "IT") est supprimé, permettant ainsi de nettoyer la collection.

![alt text](image-27.png)


