from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_de_autores = []

for pagina in range(1, 31):
    link = f"https://www.bookdepository.com/es/bestsellers?page={pagina}"

    response = requests.get(link)

    html = response.content

    soup = bs(html, "lxml")

    authors = soup.find_all("p", class_="author")
    authors_lista = [elemento.get_text() for elemento in authors]

    for i in range(len(authors_lista)):
        authors_lista[i] = authors_lista[i].replace("\n", "")

    lista_de_autores += authors_lista

    print(f"pagina {pagina} cargada")

lista_series = pd.Series(lista_de_autores)
print(lista_series.value_counts())