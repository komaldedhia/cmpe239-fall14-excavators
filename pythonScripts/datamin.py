
from urllib2 import Request, urlopen, URLError
import json
import sys
import datetime
import locale
import re
file = open('C:/Users/goudamy/Desktop/movie.txt', 'r')
file1 = open("C:/Users/goudamy/Desktop/newfile.txt", "w")
file1.write('Title,Genre,Actors,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats\n') 
for line in file:
    print line
    title1 =  line.replace(" ","%20")  
    title1 = title1.rstrip('\n')
    title2 = line.rstrip('\n')
    print title1
    link = 'http://www.omdbapi.com/?i=&t=' + title1 +'&tomatoes=true'
    print link
  
    request = Request(link)
    try:
	 response = urlopen(request)
	 j = json.load(response)	
	 print j['Title']
	 print j['Genre']
	 print j['Year']
	 print j['Actors']
	 print j['Director']
	 print j['Writer']
	 print j['imdbRating']
	 print j['Awards']
	 print j['imdbVotes']
	 print j['Country'] 
	 print j['Released'] 
	 print j['tomatoUserReviews']  
	 print j['tomatoUserRating'] 
	 print j['tomatoUserMeter'] 
	 print j['BoxOffice']
	 print j['Rated']
	 print j['Metascore']  
	#Output in JSOnN format
	#imdb = response.read()
	#print j
    except :
	   pass
    try:
     rd = j['Released']
     date_time = datetime.datetime.strptime(rd,"%d %b %Y")
     t= datetime.datetime.strftime(date_time, "%Y-%m-%d")
     Dates = t.split()  
     Year= Dates[0][0:4]
     Month = Dates[0][5:7]
     t = Year+Month
     wiki_url = 'http://stats.grok.se/json/en/'+t+'/'+title2
     print wiki_url
     wiki_read = json.loads(urlopen(wiki_url).read())
     total_views = sum([count for count in wiki_read['daily_views'].values()])
     total_str =str(total_views)
     print total_str
     #resultant = j['Title'] +','+ j['Genre']+','+j['Year']+','+j['Actors']+','+j['Director']+','+j['Writer']+','+j['imdbRating']+','+j['Awards']+','+j['imdbVotes']+','+j['Country']+',' +j['Released'] +','+j['tomatoUserReviews']+',' +j['tomatoUserRating']+',' +j['tomatoUserMeter']+',' +j['BoxOffice'] +','+total_views
     if j['BoxOffice'] != 'N/A':     
     	box = j['BoxOffice'].replace("M","") 
     	box = box.replace("$","") 
        imdb_genre = j['Genre'].replace(",","-")
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
        if 'USA' in j['Country']:
      	  resultant = j['Title'] +','+ imdb_genre +','+ imdb_Actors +','+ imdb_Production +','+imdb_Director +','+imdb_Awards +','+imdb_rating +',' + imdb_votes + ','+j['Released']+','+ tomatoUserReviews +','+tomatoUserRating+','+tomatoUserMeter+',' + box+','+Rated+','+Metascore
          file1.write( resultant  +','+ total_str + "\n")
     
    except:
    	pass
#t = datetime.date.today()
#t = "%s%02i" % (t.year, t.month)
file1.close()    

