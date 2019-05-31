import bs4
import re
import urllib.request
from bs4 import BeautifulSoup as soup
count = 1
#Pass the URL as the parameter? Or pass the player first and last and use the DevaSe00 format to predict?

filename = "2019UDFA.csv"
f = open(filename, "w")
headers = ("Player|Position|College|NFL_Team|Years|Dollars|Guaranteed|2019_CAP\n")
f.write(headers)

#Location of SethDeValve's Profootball Reference Page
my_url = 'http://www.spotrac.com/nfl/undrafted-free-agents/'



#open connection, retrieve html and store in page_html. Close Connection.
uClient = urllib.request.Request(my_url)
page_html=urllib.request.urlopen(uClient)
#uClient.close()


#parse the html
page_soup = soup(page_html, "html.parser")

#result_Container = container.findAll(href=re.compile("http://www.spotrac.com/redirect/player/")) EXTRA LINKS IN TRENDING PLAYERS SECTION
#gameYear_Container = container.findAll("td", {"data-stat":"year_id"})
containers = page_soup.findAll("tr")

for container in containers:

	if count != 1:
	
		#Player
		print("CONTAINER START")
		print (container)
		print("CONTAINER END")
		
		#Player
		player_Container = container.findAll("td", {"class":"player"}) 
		player = player_Container[0].text
		print("PLAYER: " + player)
		#print(player)
		
		#Position
		position_Container = container.findAll("td", {"class":"center"})
		position = position_Container[0].text
		print("POSITION: " + position)
	
		#College
		college_Container = container.findAll("td", {"class":"center"})
		college = college_Container[0].text
		print("COLLEGE: " + college)	
	
		#Team
		team = college_Container[1].text
		print("TEAM: " + team)	
	
		#Years
		years = college_Container[2].text
		print("YEARS: " + years)	
	
		#Dollars
		dollars_Container = container.findAll("td", {"class":"right"}) 
		dollars = dollars_Container[0].text
		print("DOLLARS: " + dollars)	
		
		#Guaranteed
		guaranteed = dollars_Container[1].text
		print("GUARANTEED: " + guaranteed)	
		
		#2018_Cap
		cap_Container = container.findAll("td", {"class":"right hidden-xs"}) 
		cap = cap_Container[0].text
		print("CAP: " + cap)
		
		f.write(player + "|" + position + "|" + college + "|" + team + "|" + years + "|" + dollars + "|" + guaranteed + "|" + cap + "\n")
		
	count = count + 1
	
	
f.close()