import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
directorColl = db.topDirectors

f = open('E:/239 mining/Project/Goudamy/topDirectors.csv')
csv_f = csv.reader(f)
seq = 0

for row in csv_f:
        
        directors=row[0]
        director = directors.strip()
        print director
        query = {"director":director}
        doc = directorColl.find_one(query)
        if doc is None:
            seq = seq + 1
            query = {"director":director,"_id":seq}
            directorColl.insert(query)
        else:
            print doc
        
           
print("Max Actors in the list "+`seq`)
            
    