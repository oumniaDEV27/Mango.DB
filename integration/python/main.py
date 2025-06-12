# integration/python/tests/main.py
from pymongo import MongoClient

# Connexion à une base standalone
client = MongoClient("mongodb://localhost:27017/")
db = client.testdb

# Insertion
db.services.insert_one({"name": "Comptabilité"})

# Lecture
for doc in db.services.find({"name": "Comptabilité"}):
    print(doc)

# Mise à jour
update_result = db.services.update_one({"name": "Comptabilité"}, {"$set": {"name": "IT"}})
print("Nombre de documents mis à jour :", update_result.modified_count)

# Suppression
delete_result = db.services.delete_one({"name": "IT"})
print("Nombre de documents supprimés :", delete_result.deleted_count)

