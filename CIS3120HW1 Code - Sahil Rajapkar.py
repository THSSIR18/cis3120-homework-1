#CIS 3120 Homework #1 Web Scraping

#searching for elements by class
#the goal of this exercise is to scrape all of the heights of the men's swimming team and export them to a file
#import requests library
import requests
from bs4 import BeautifulSoup

#defining the URL and making a GET request
#url for the site we wish to scrape
#site url for scraping
URL1 = 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster'
URL2 = 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster'
URL3 = 'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster'
URL4 = 'https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster'

#storing the content returned from the server in an object called page1
#note for servers with certain security features (good to know), you must set the verify flag to False
#making request 
page1 = requests.get(URL1, verify=False)
page2 = requests.get(URL2, verify=False)
page3 = requests.get(URL3, verify=False)
page4 = requests.get(URL4, verify=False)

#print text from our site's url
#print(page1.text) 

#importing the HTML returned from the server into beautiful soup
soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')
soup3 = BeautifulSoup(page3.content, 'html.parser')
soup4 = BeautifulSoup(page4.content, 'html.parser')

#gives the heights with spans
mensswimteamheightlist = soup1.find_all('span', class_="sidearm-roster-player-height")
mensvolleyballteamheightlist = soup2.find_all('span', class_="sidearm-roster-player-height")
womensswimteamheightlist = soup3.find_all('span', class_="sidearm-roster-player-height")
womensvolleyballteamheightlist = soup4.find_all('span', class_="sidearm-roster-player-height")

def average(heightlist100):
    mylist = []
    for x in heightlist100:
        height = x.get_text()
        mylist.append(height)
        #print(mylist)
        #height = s.strip('"\"') for s in mylist  # remove the \ from the string 
        #mylst = map(lambda each:each.strip("'\'"), mylist)
    lst = mylist
        #print([s.strip('"') for s in lst]) # remove the \ and " from the string borders
        #LET'S GOOOOOOOO, HERE I GOT THE HEIGHTS OF EACH OF THE TEAMS USING A FUNCTION!!!!!!!!!!!
    new_list = [s.replace("\"", "") for s in lst]
    #LET'S GOOOOOOO AGAIN, I GOT THE HEIGHTS WITHOUT THAT \ TO COME WITH IT TOOO
    #Create a new list from the one below by converting each height to inches

    height = new_list

    #The new list will look like the following: [70, 71, 69, 75...]

    #1 foot = 12 inches

    #Someone whos is 5'10" is 70 inches tall. Why 5 * 12 = 60 inches and if I add 10 inches I get 70


    heights_in_inches1 = []

    for i in range(0, len(height)):
      #splitting the raw string on the '
      x = height[i].split("'")
      #extracting the feet from the splitted list and converting to int

      feet = int(x[0])
      #converting the feet to inches by mulitplying it by 12

      feet_as_inches = feet * 12
      ##extracting the inches from the splitted list and converting to int

      inches = int(x[1])
      #calculating the total height inches

      total_height_in_inches =  feet_as_inches + inches

      #appending the converted height to a new list
      heights_in_inches1.append(total_height_in_inches)

    #printing the heights in inches (no need to print it really)
    heights_in_inches1

    #find the average height (no need to print once again just for calculation)
    print(sum(heights_in_inches1) / len(heights_in_inches1))
    
average(mensswimteamheightlist)
average(mensvolleyballteamheightlist)
average(womensswimteamheightlist)
average(womensvolleyballteamheightlist) 

#answers to questions
# (1) The average of the men's swimming team is roughly 71.27 inches
# (2) The average of the men's volleyball team is roughly 73.53 inches
# (3) The average of the women's swim team is 64.2 inches
# (4) The average of the women's volleyball team is roughly 65.33 inches
# (5) I found out that the average of the men's volleyball team was > than that of the men's swim team by about 2.26 inches
# (6) I found out that the average of the women's volleyball team is also > than that of the women's swim team by about 1.13 inches
# The trend here is that the average height of the overall volleyball team would be great than the swim
# This trend makes sense because overall you can insinuate that a volleyball player is taller than a swimmer
# (7) No, overall, the average volleyball player is taller than the average swimmer


#the graveyard
#print("The average height of the men's swim team=", average(mensswimteamheightlist))
#print("The average height of the men's volleyball team=", average(mensvolleyballteamheightlist))
#print("The average height of the women's swim team=", average(womensswimteamheightlist))
#print("The average height of the women's volleyball team=", average(womensvolleyballteamheightlist))

#the graveyard
#basically this works but the problem is we need to figure out how to convert the string of lists into ints
#we have the average heights of the men's swimming team in inches!!!!!!!!!!!!!!!!
#now I think I need to use a "def" function to loop thorught hte URLs in a data structure such as lists, dictionaries, etc.
#driving code
#lst100 = heights_in_inches1
#average = Average(lst100)

#print("Average height of the men's swimming team=", round(average,2)) 
#print("Average height of the men's volleyball team=", round(average,2)) 
#print("Average height of the women's swimming team=", round(average,2)) 
#print("Average height of the women's volleyball team=", round(average,2)) 

#basically this works but the problem is we need to figure out how to convert the string of lists into ints

#soup.find_all('span', class_="height") parses the html and collects all of the 'a' tags which are assigned an "height class"
#we convert the value returned by soup.find_all('span', class_="sidearm-list-player-height") to a list and then store it in heightList
# Function definition is here
#def removethecharacters(heightlist1000):
 #  "This prints a passed list into this function"
  #  new_list = [s.replace("\"", "") for s in lst]:
   # print(new_list)
#removethecharacters(mensswimteamheightlist)
#removethecharacters(mensvolleyballteamheightlist)
#showhei(womensswimteamheightlist)
#showheights(womensvolleyballteamheightlist)
     
#accorinding to Theophilus comment, I should be using both for loops and functions
#at the moment, I only have a loop that shows the heights of everyone on the mens' swim team
   # mylist = []
   # for w in mensswimteamheightlist:
   # height = w.get_text()
   # mylist.append(height)
  #print(mylist)
  #height = s.strip('"\"') for s in mylist  # remove the \ from the string 
  #mylst = map(lambda each:each.strip("'\'"), mylist)
    #lst = mylist
   # print(lst)

#print([s.strip('"') for s in lst]) # remove the \ and " from the string borders

#print(type(lst[0]))

#([s.strip('"') for s in lst]) # remove the \ and " from the string borders
#we need to put the new lsit of heights without the \ in a list

#new_list = [s.replace("\"", "") for s in lst]
#print(new_list)

  # return;

#mensswimteamheightlist = []
#mensvolleyballteamheightlist = []
#womensswimteamheightlist = []
#womensvolleyballteamheightlist = []

#removethecharacters(mensswimteamheightlist)
#removethecharacters(mensvolleyballteamheightlist)
#removethecharacters(womensswimteamheightlist)
#removethecharacters(womensvolleyballteamheightlist)

#hint: 
#inspect the html on each page listed above. Determine which tag and class point to the players’ heights. 
#the tasks listed here span many different topics in python. (There’s a huge clue in the previous
#sentence!)

#class : "sidearm-list-player-height" for the player
#tag: "span" tag for each player

#let's take a look at men's swim team height list