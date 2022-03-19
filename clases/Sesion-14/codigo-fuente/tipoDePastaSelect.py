from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

link = "https://www.bookdepository.com/es/bestsellers"
response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

formats = soup.select("div.item-info p.format")
formats_text = [elemento.get_text() for elemento in formats]

formats_serie = pd.Series(formats_text)
print(formats_serie.value_counts())