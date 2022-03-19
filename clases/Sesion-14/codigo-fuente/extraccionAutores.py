from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

link = "https://www.bookdepository.com/es/bestsellers"

response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

authors = soup.find_all("p", class_="author")
authors_lista = [elemento.get_text() for elemento in authors]

for i in range(len(authors_lista)):
    authors_lista[i] = authors_lista[i].replace("\n", "")

print(authors_lista)