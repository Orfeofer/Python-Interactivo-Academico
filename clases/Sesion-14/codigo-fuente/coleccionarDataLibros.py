from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

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

lista_titulo = []
lista_autores = []
lista_fecha = []
lista_pasta = []
lista_precio = []

for pagina in range(1, 10):
    link = "https://www.bookdepository.com/es/bestsellers?page={pagina}"
    response = requests.get(link)

    html = response.content

    soup = bs(html, "lxml")

    ################################ TITULOS ################################ 

    lista_titulos = soup.find_all("h3", class_="title")
    lista_titulos_formato = []
    for elemento in lista_titulos:
        lista_titulos_formato.append(elemento.get_text())

    for i in range(len(lista_titulos_formato)):
        lista_titulos_formato[i] = lista_titulos_formato[i].replace("\n", "")
        lista_titulos_formato[i] = quitar_espacios_iniciales(lista_titulos_formato[i])
    lista_titulo += lista_titulos_formato

    ################################ AUTORES ################################ 

    authors = soup.find_all("p", class_="author")
    authors_lista = [elemento.get_text() for elemento in authors]

    for i in range(len(authors_lista)):
        authors_lista[i] = authors_lista[i].replace("\n", "")

    lista_autores += authors_lista
    ################################ FECHA ################################ 

    fechas = soup.find_all("p", class_="published")
    fechas_lista = [elemento.get_text() for elemento in fechas]

    lista_fecha += fechas_lista
    ################################ PASTA ################################ 

    formats = soup.find_all("p", class_="format")
    formats_text = [elemento.get_text() for elemento in formats]


    lista_pasta += formats_text
    ################################ PRECIO ################################

    precios = soup.find_all("p", class_="price")
    precios_texto = [elemento.get_text() for elemento in precios]

    for i in range(len(precios_texto)):
        precios_texto[i] = precios_texto[i].replace("\n", "")
        precios_texto[i] = quitar_espacios_iniciales(precios_texto[i])
        precios_texto[i] = seleccionar_precio(precios_texto[i])

    lista_precio += precios_texto
    ############################################################################
    print(f"pagina {pagina}")

titulos_serie = pd.Series(lista_titulo)
autores_serie = pd.Series(lista_autores)
fechas_serie = pd.Series(lista_fecha)
pasta_serie = pd.Series(lista_pasta)
precio_serie = pd.Series(lista_precio)

data = pd.DataFrame({"Titulo": titulos_serie,
                     "Autor": autores_serie,
                     "Fecha de publicacion": fechas_serie,
                     "Tipo de pasta": pasta_serie,
                     "Precio": precio_serie})

#data.reset_index(drop=True, inplace=True)

data.to_excel("dataLibros.xlsx")