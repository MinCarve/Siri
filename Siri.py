import webbrowser
import random
import datetime

browserSearch = False
time = datetime.datetime.now()
search = "search"
i = random.randint(0, 1)
options = [time, search]

_options = options[i]

if _options == time:
    browserSearch = False
    print(time)

elif _options == search:
    browserSearch = True

if browserSearch == True:
    browserurl = "https://google.com/#q="

    search = input("Enter a keyword to search \n")
    search = '+'.join(search.split())

    webbrowser.open(browserurl + search)
