import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
prodColl = db.prodHouse

f = open('E:/239 mining/Project/Goudamy/ProductionHouse.csv')
csv_f = csv.reader(f)
maxProHouse = 0
lineCnt = 0
seq = 0

for row in csv_f:
    
    prodHouse=row[0].strip()
    #actorList = actors.split("-")
    print prodHouse
    #actor = actors.strip()
    #print actor
    query = {"prodHouse":prodHouse}
    doc = prodColl.find_one(query)
    if doc is None:
        seq = seq + 1
        query = {"prodHouse":prodHouse,"_id":seq}
        prodColl.insert(query)
    else:
        print doc

   
        
           
    