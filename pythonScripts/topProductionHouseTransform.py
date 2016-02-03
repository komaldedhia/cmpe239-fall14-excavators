import csv
import pymongo
from pymongo import MongoClient

connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")
prodColl = db.topProdHouse

f = open('E:/239 mining/Project/Goudamy/Transformed/genreTransform.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/topProdHouseTransform.csv','wb')
csv_f = csv.reader(f)
writer = csv.writer(j)
#actList=[0,0,0,0,0,0]
lineCnt = 0
j.write('Title,Genre,Actor,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n')
for row in csv_f:
    lineCnt = lineCnt + 1
    if lineCnt > 1:
        prod=row[5]
        prodList = prod.split("/")
        cnt = 0
        #print actorList
        for prodHouse in prodList:
            cnt = cnt+ 1
            if (cnt == 1):
                productioHouse = prodHouse.strip()
                #print productioHouse
                if "Screen Media" in productioHouse:
                    productioHouse="SMedia"
                elif "Screen Gems" in productioHouse:
                    productioHouse="SGems"
                elif "Open Road Films" in productioHouse:
                    productioHouse = "OpRd"
                elif "Metro-Goldwyn-Mayer" in productioHouse:
                    productioHouse ="MGM"
                elif  "FilmBuff" in productioHouse:
                    productioHouse = "Buff"
                elif "Tribeca" in productioHouse:
                    productioHouse = "Tribecca"
                elif "FilmDistrict" in productioHouse:
                    productioHouse="District"
                elif "New Films" in productioHouse:
                    productioHouse = "NeFm"
                elif "LD Entertainment"  in productioHouse:
                    productioHouse = "LDEnte"
                elif "Vitagraph" in productioHouse:
                    productioHouse ="ViGrp"
                elif "Area 23a"   in productioHouse:
                    productioHouse = "Area23A"
                elif "Arc Entertainment"   in productioHouse:
                    productioHouse = "ArcEn"
                elif "FilmDisctrict" in productioHouse:
                    productioHouse = "District"
                elif "High Top" in productioHouse:
                    productioHouse="Hightop"
                elif "Millennium"  in productioHouse:
                    productioHouse="Milennium"
                elif "Radius-TWC" in productioHouse:
                    productioHouse="Radius"
                elif "World Wide"in productioHouse:
                    productioHouse="WrlWid"
                elif "First Independent Pictures" in productioHouse:
                    productioHouse = "FirInde"
                elif "New Line Cinema" in productioHouse:
                    productioHouse = "Warner"
                elif "TriStar" in productioHouse:
                    productioHouse = "Sony"
                elif "Stage 6" in productioHouse:
                    productioHouse = "Sony"
                elif "Touchstone Pictures" in productioHouse:
                    productioHouse = "Walt"
                elif "Disneynature"in productioHouse:
                    productioHouse = "Walt"
                elif "Focus Features"in productioHouse:
                    productioHouse = "Universal"
                elif "Nickelodeon" in productioHouse:
                    productioHouse = "Paramount"
                elif "Roadside" in productioHouse:
                    productioHouse = "Lionsgate"
                elif "Dimension" in productioHouse:
                    productioHouse = "Weinstein"
                    
                
                doc = db.command("text", "topProdHouse",search=productioHouse, project={"_id": 1})
                #query = {"prodHouse":productioHouse}
                #colums = {"_id":1}
                #doc = prodColl.find_one(query,colums)
                #print doc
                #if doc == []:
                rs = doc['results']
                #print rs
                if rs == []:
                    
                    prodHouseId=0
                else:
                    print productioHouse
                    prodHouseId=1
                new_row = [row[0],row[1],row[2],row[3],row[4],prodHouseId,row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
                writer.writerow(new_row)