from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

link = "https://www.bookdepository.com/es/bestsellers"
response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

fechas = soup.find_all("p", class_="published")
fechas_lista = [elemento.get_text() for elemento in fechas]

fechas_serie = pd.Series(fechas_lista)
print(fechas_serie.value_counts())