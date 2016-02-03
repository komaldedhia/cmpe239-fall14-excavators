import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
actorsColl = db.topActors

f = open('E:/239 mining/Project/Goudamy/topActorsv1.csv')
csv_f = csv.reader(f)
seq = 0

for row in csv_f:
        
        actors=row[0]
        actor = actors.strip()
        print actor
        query = {"actor":actor}
        doc = actorsColl.find_one(query)
        if doc is None:
            seq = seq + 1
            query = {"actor":actor,"_id":seq}
            actorsColl.insert(query)
        else:
            print doc
        
           
print("Max Actors in the list "+`seq`)
            
    