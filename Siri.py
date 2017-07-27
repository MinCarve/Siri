import webbrowser
import random

browserurl = "https://google.com/#q="

search = input("Enter a keyword to search \n")

search = '+'.join(search.split())

webbrowser.open(browserurl + search)
