import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
genreColl = db.genre

f = open('E:/239 mining/Project/Goudamy/Transformed/total_title_result_out.csv')
csv_f = csv.reader(f)
maxProHouse = 0
lineCnt = 0
seq = 0

for row in csv_f:
    
    genre=row[1].strip()
    #actorList = actors.split("-")
    print genre
    #actor = actors.strip()
    #print actor
    query = {"genre":genre}
    doc = genreColl.find_one(query)
    if doc is None:
        seq = seq + 1
        query = {"genre":genre,"_id":seq}
        genreColl.insert(query)
    else:
        print doc