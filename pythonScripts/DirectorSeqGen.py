import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
directorColl = db.directors

f = open('E:/239 mining/Project/Goudamy/Transformed/prodHouseTransform.csv')
csv_f = csv.reader(f)
maxDirectors = 0
lineCnt = 0
seq = 0

for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        cnt = 0
        directors=row[3]
        directorList = directors.split("-")
        print directorList
        for r in directorList:
            cnt = cnt+ 1
            director = r.strip()
            if cnt <3:
                print director
                query = {"director":director}
                doc = directorColl.find_one(query)
                if doc is None:
                    seq = seq + 1
                    query = {"director":director,"_id":seq}
                    directorColl.insert(query)
                else:
                    print doc
            
        if cnt>maxDirectors:
            maxDirectors=cnt
        
print("Max Actors in the list "+`maxDirectors`)
            
    