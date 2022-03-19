import requests
from bs4 import BeautifulSoup as bs

link = "https://www.autocosmos.com.pe/auto/usado"
response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

title = soup.find_all("span",class_ = "listing-card__brand")
title_lista = [elemento.get_text() for elemento in title]

print(title_lista)