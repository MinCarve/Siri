import webbrowser
import random
import datetime
import os

browserSearch = False
youtubeSearch = False
time = datetime.datetime.now()
gsearch = "search"
ytsearch = "ytsearch"
weather = "weather"
yelp = "yelp"
reddit = "reddit"
i = random.randint(0, 5)
options = [time, ytsearch, gsearch, weather, yelp, reddit]

_options = options[i]

if _options == reddit:
    redditURL = "https://www.reddit.com/search?q="

    _reddit = input("What would you like to browse for on Reddit? \n")
    _reddit = '+'.join(_reddit.split())
    webbrowser.open(redditURL + _reddit)

if _options == yelp:
    YelpURL = "https://www.yelp.com/search?find_desc="
    
    _yelp = input("What would you like to eat? \n")
    _yelp = '+'.join(_yelp.split())
    webbrowser.open(YelpURL + _yelp)
    

if _options == weather:
    _weather = input("Would you like to find out the weather in your local area?  [Y/N] \n")
    if _weather == "Y" or _weather == "y":
        webbrowser.open("https://duckduckgo.com/?q=weather&t=raspberrypi&ia=weather")
    elif _weather == "N" or _weather == "n":
        os._exit(1)
    else:
        print("Please enter Y for yes or N for no")

if _options == time:
    print("The date and time is")
    print(time)

elif _options == gsearch:
    browserSearch = True

elif _options == ytsearch:
    youtubeSearch = True

if youtubeSearch == True:
    yturl = "https://youtube.com/results?search_query="

    ytsearch = input("What video do you want to watch? \n")
    ytsearch = '+'.join(ytsearch.split())
    
    webbrowser.open(yturl + ytsearch)

if browserSearch == True:
    browserurl = "https://google.com/#q="

    search = input("Enter a keyword to search the web \n")
    search = '+'.join(search.split())

    webbrowser.open(browserurl + search)
