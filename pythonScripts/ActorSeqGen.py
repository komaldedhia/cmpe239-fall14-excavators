import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
actorsColl = db.actors

f = open('E:/239 mining/Project/Goudamy/Transformed/prodHouseTransform.csv')
csv_f = csv.reader(f)
maxActors = 0
lineCnt = 0
seq = 0

for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        cnt = 0
        actors=row[2]
        actorList = actors.split("-")
        print actorList
        for actors in actorList:
            cnt = cnt+ 1
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
            
        if cnt>maxActors:
            maxActors=cnt
        
print("Max Actors in the list "+`maxActors`)
            
    