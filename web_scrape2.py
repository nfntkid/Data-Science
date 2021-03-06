from bs4 import BeautifulSoup as bfs
import requests as rq
import re
#load webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = rq.get(url + "webpage.html")
#r = rq.get("https://www.binance.com/en/markets")

#convert to a BeautifulSoup Object
webpage = bfs(r.content)
images = (webpage.select("div.row div.column img"))
image_url = images[0]['src']
full_url = url + image_url


# Download the image
img_data = rq.get(full_url).content
with open("lake_como.jpg","wb") as handler:
    handler.write(img_data)
