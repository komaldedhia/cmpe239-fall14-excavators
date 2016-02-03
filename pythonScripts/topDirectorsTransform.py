import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
direColl = db.topDirectors

f = open('E:/239 mining/Project/Goudamy/Transformed/topActorTransform.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/topActorDirectorProd.csv','wb')
csv_f = csv.reader(f)
writer = csv.writer(j)
direList=[0,0,0]
lineCnt = 0
j.write('Title,Genre,Actor,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n')
for row in csv_f:
    lineCnt = lineCnt + 1
    topDirectorCount =0
    if lineCnt > 1:
        dires=row[3]
        direList = dires.split("-")
        for directors in direList:
            director = directors.strip()
           
            query = {"director":director}
            colums = {"_id":1}
            doc = direColl.find_one(query,colums)
            if doc is None:
                print director
            else:
                topDirectorCount = topDirectorCount+1
            
        new_row = [row[0],row[1],row[2],topDirectorCount,row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
        writer.writerow(new_row)
        direList=[0,0,0]