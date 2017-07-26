import webbrowser
import random
import pyttsx

engine = pyttsx.init()

browserurl = "https://google.com/#q="

engine.say("Enter a keyword to search")
engine.runAndWait()

search = input("Enter a keyword to search \n")

search = '+'.join(search.split())

webbrowser.open(browserurl + search)
