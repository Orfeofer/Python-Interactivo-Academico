from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def quitar_espacios_iniciales(cadena):
    indice = 0
    for letra in cadena:
        if(letra == " "):
            indice += 1
        else:
            break
    return cadena[indice:]

def seleccionar_precio(cadena):
    indice = 0
    for letra in cadena:
        if(letra != " "):
            indice += 1
        else:
            break
    return cadena[:indice]

link = "https://www.bookdepository.com/es/bestsellers"

response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

precios = soup.find_all("p", class_="price")
precios_texto = [elemento.get_text() for elemento in precios]

for i in range(len(precios_texto)):
    precios_texto[i] = precios_texto[i].replace("\n", "")
    precios_texto[i] = quitar_espacios_iniciales(precios_texto[i])
    precios_texto[i] = seleccionar_precio(precios_texto[i])

print(precios_texto)