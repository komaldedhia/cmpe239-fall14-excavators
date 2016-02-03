import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
actorsColl = db.actors

f = open('E:/239 mining/Project/Goudamy/Transformed/prodHouseTransform.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/actorTransform.csv','wb')
csv_f = csv.reader(f)
writer = csv.writer(j)
actList=[0,0,0,0,0,0]
lineCnt = 0
j.write('Title,Genre,Actor1,Actor2,Actor3,Actor4,Actor5,Actor6,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n')
for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        actors=row[2]
        actorList = actors.split("-")
        cnt = -1
        #print actorList
        for actors in actorList:
            cnt = cnt+ 1
            actor = actors.strip()
            print actor
            query = {"actor":actor}
            colums = {"_id":1}
            doc = actorsColl.find_one(query,colums)
            actorId = doc['_id']
            print doc['_id']
            actList [cnt]= actorId
        print actList
        new_row = [row[0],row[1],actList[0],actList[1],actList[2],actList[3],actList[4],actList[5],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
        writer.writerow(new_row)
        actList=[0,0,0,0,0,0]