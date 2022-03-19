from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

link = "https://www.bookdepository.com/es/bestsellers"
response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

formats = soup.find_all("p", class_="format")

###################
formats_text = [elemento.get_text() for elemento in formats]
###############

# #########
# formats_text = []
# for elemento in formats:
#     formats_text.append(elemento.get_text())
# #########

pandas_format = pd.Series(formats_text)

print(pandas_format.value_counts())