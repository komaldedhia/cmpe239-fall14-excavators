from flask import Flask,render_template,request,url_for
from urllib2 import Request, urlopen, URLError
import json
import sys
import datetime
import locale
import re
from py4j.java_gateway import JavaGateway
from pymongo import MongoClient
app = Flask(__name__)
connection = MongoClient('ds047800.mongolab.com',47800)
db = connection.moviedb
db.authenticate("cmpe239", "cmpe239")

prodColl = db.topProdHouse
actorsColl = db.topActors
direColl = db.topDirectors
genreColl = db.genre

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')     

@app.route('/movie', methods=['POST'])
def index():
    movie = request.form['movie']
    print movie
    imdbTitle =  movie.replace(" ","%20")
    link = 'http://www.omdbapi.com/?i=&t=' + imdbTitle +'&tomatoes=true'      
    linkRequest = Request(link)
    try:
        
        linkResponse = urlopen(linkRequest)
        j = json.load(linkResponse)    
        print j['Title']    
     
    except :
        pass
        return render_template('index.html',errMsg="Pls Enter Correct Movie")
    try:
        rd = j['Released']
        date_time = datetime.datetime.strptime(rd,"%d %b %Y")
        t= datetime.datetime.strftime(date_time, "%Y-%m-%d")
        Dates = t.split()  
        Year= Dates[0][0:4]
        Month = Dates[0][5:7]
        t = Year+Month 
        try:
            wiki_url = 'http://stats.grok.se/json/en/'+t+'/'+movie
            print wiki_url
            wiki_read = json.loads(urlopen(wiki_url).read())
            total_views = sum([count for count in wiki_read['daily_views'].values()])
            total_str =str(total_views)
            print total_str
        except :
            pass
                    
        imdb_genre = j['Genre'].replace(",","-")
        j['Title'] = j['Title'].replace(",","-")
        imdb_Actors = j['Actors'].replace(",","-") 
        imdb_Director = j['Director'].replace(",","-") 
        imdb_Awards = j['Awards'].replace(",","-") 
        imdb_Production = j['Production'].replace(",","-")   
        imdb_votes = j['imdbVotes'].replace(",","") 
        tomatoUserReviews = j['tomatoUserReviews'].replace(",","") 
        tomatoUserRating = j['tomatoUserRating'].replace(",","") 
        tomatoUserMeter = j['tomatoUserMeter'].replace(",","") 
        imdb_rating = j['imdbRating'].replace(",","")
        Rated = j['Rated'].replace(",","")
        Metascore = j['Metascore'].replace(",","")
        print "*********"
        if 'USA' in j['Country']:
            print "comin"
            resultant = j['Title'] +','+ imdb_genre +','+ imdb_Actors +','+imdb_Director +','+imdb_Awards+',' +imdb_Production+','+imdb_rating +',' + imdb_votes + ','+j['Released']+','+ tomatoUserReviews +','+tomatoUserRating+','+tomatoUserMeter                 
            print resultant   
        else:
            return render_template('index.html',errMsg="Pls Enter USA Movie")
    except:
            return render_template('index.html',errMsg="Pls Enter Correct Movie")
    try:
        genre=imdb_genre.strip()             
        query = {"genre":genre}
        colums = {"_id":1}
        doc = genreColl.find_one(query,colums)
        if doc is None:
            genreId=0 
        else:
            genreId = doc['_id']
        print "genre Id " + `genreId`
        
        topActorCount=0
        actors=imdb_Actors
        actorList = actors.split("-")
        for actors in actorList:
            actor = actors.strip()           
            query = {"actor":actor}
            colums = {"_id":1}
            doc = actorsColl.find_one(query,colums)
            if doc is None:
                print actor
            else:
                topActorCount = topActorCount+1
        print "topActorCount "+`topActorCount`
        
        topDirectorCount=0
        imdb_Director = j['Director'].replace(",","-") 
        dires=imdb_Director
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
                
        print("topDirectorCount "+`topDirectorCount`)
        
        
         
        prod=imdb_Production
        prodList = prod.split("/")
        cnt = 0
           
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
                    rs = doc['results']
                    #print rs
                    if rs == []:
                        
                        prodHouseId=0
                    else:
                        print productioHouse
                        prodHouseId=1
            
        print "prodHouseId "+`prodHouseId` 

    except:
            return render_template('index.html',errMsg="Errroe while transforming the data")
        
    gateway = JavaGateway() 
    predictionModel = gateway.entry_point

    #Genre Production Released Actor Director imdbRating Metascore Wikistats BoxOffice */
    output=predictionModel.boxOfficePre(str(genreId),str(prodHouseId),"1",str(topActorCount),str(topDirectorCount),imdb_rating,Metascore,total_str)
    print "Hi "+`output`
    boxOfficeValue=""
    if output==0.0:
        boxOfficeValue="181--200000"
    elif output==1.0:
        boxOfficeValue="200000--5000000"
    elif output==2.0:
        boxOfficeValue="5000000--20000000"
    elif output==3.0:
        boxOfficeValue="20000000--40000000"
    elif output==4.0:
        boxOfficeValue="40000000--80000000"
    elif output==5.0:
        boxOfficeValue="80000000--760500000"
        
    
    return render_template('predict.html',boxOffice=boxOfficeValue)
 
if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 9000)
