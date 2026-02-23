#Page Title (without any HTML tags)

#Page Body (just the text, without any html tags)

#All the URLs that the page points/links to

import requests
from bs4 import BeautifulSoup
import sys
try:
    url = sys.argv[1]
except IndexError:
    print("Error: No URL provided. Please provide a URL as a command line argument.")
    sys.exit()

r = requests.get(url)   
soup = BeautifulSoup(r.text, 'html.parser') 
title = soup.find('title')
if title:
    print(title.get_text())
else:
    print("No title found")
print()
body = soup.find('body')
if body:
    text = body.get_text()
    clean_text = " ".join(text.split())
    print(clean_text)
else :
    print("No body found")
links = soup.find_all('a', href=True)
print("Links:")
for link in links:
    print(link['href'])
