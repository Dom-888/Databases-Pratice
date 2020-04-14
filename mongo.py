import pymongo

import os

MONGODB_URI = os.getenv("MONGO_URI") # Variabile ambientale precedentemente inserita in .bashrc
DBS_NAME = "myTestDB" 
COLLECTION_NAME = "myFirstDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connect!")
        return conn
    except pymongo.error.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

# La variabile coll permette di manipolare il database usando i MongoDB metods: coll.method()
coll = conn[DBS_NAME][COLLECTION_NAME]


# Examples:

# Insert a new object in the collection
new_doc = {'first': 'Douglas', 'last': 'Adams', 'dob': '11/03/1952', 'hair_colour': 'purple', 'occupation': 'writer', 'nationality': 'english'}
coll.insert_one(new_doc) # To insert more than one object from a list use the insert_many() method

# Updare an object from the collection, to remove use the delete_one() method
documents = coll.update_one({'first': 'Rocky'}, {'$set': {'hair_colour': 'vantablack'}})

# Print the collection in the terminal
documents = coll.find()  
for doc in documents:
    print(doc)