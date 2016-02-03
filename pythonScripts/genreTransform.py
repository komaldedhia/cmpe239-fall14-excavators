import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
genreColl = db.genre

f = open('E:/239 mining/Project/Goudamy/Transformed/total_title_result_out.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/genreTransform.csv','wb')
csv_f = csv.reader(f)
writer = csv.writer(j)
lineCnt = 0
j.write('Title,Genre,Actor,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n')
for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        genre=row[1].strip()
             
        query = {"genre":genre}
        colums = {"_id":1}
        doc = genreColl.find_one(query,colums)
        genreId = doc['_id']
        new_row = [row[0],genreId,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
        writer.writerow(new_row)
        
        
print "done"