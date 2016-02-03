import csv
import pymongo
from pymongo import MongoClient
from py4j.java_gateway import JavaGateway

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
directorColl = db.directors
gateway = JavaGateway() 

f = open('E:/239 mining/Project/Goudamy/Transformed/actorTransform.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/actorDirctorProdTransform1.csv','wb')
csv_f = csv.reader(f)
writer = csv.writer(j)
direList=[0,0]
lineCnt = 0
j.write('Title,Genre,Actor1,Actor2,Actor3,Actor4,Actor5,Actor6,Director1,Director2,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n')
for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        directors=row[8]
        directorsList = directors.split("-")
        cnt = -1
        #print actorList
        for r in directorsList:
            cnt = cnt+ 1
            if cnt<=1:
                director = r.strip()
                print director
                query = {"director":director}
                colums = {"_id":1}
                doc = directorColl.find_one(query,colums)
                print doc
                directorId = doc['_id']
                print doc['_id']
                direList [cnt]= directorId
        print direList
        new_row = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],direList [0],direList [1],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20]]
        writer.writerow(new_row)
        direList=[0,0]