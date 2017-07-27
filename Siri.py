import webbrowser
import random
import datetime

browserSearch = False
youtubeSearch = False
time = datetime.datetime.now()
gsearch = "search"
ytsearch = "ytsearch"
i = random.randint(0, 2)
options = [time, ytsearch, gsearch]

_options = options[i]

if _options == time:
    print("The date and time is")
    print(time)

elif _options == gsearch:
    browserSearch = True

elif _options == ytsearch:
    youtubeSearch = True

if youtubeSearch == True:
    yturl = "https://youtube.com/results?search_query="

    ytsearch = input("What video do you want to watch?")
    ytsearch = '+'.join(ytsearch.split())
    
    webbrowser.open(yturl + ytsearch)

if browserSearch == True:
    browserurl = "https://google.com/#q="

    search = input("Enter a keyword to search the web \n")
    search = '+'.join(search.split())

    webbrowser.open(browserurl + search)
