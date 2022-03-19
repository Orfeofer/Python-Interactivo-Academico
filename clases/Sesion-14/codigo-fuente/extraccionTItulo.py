from bs4 import BeautifulSoup as bs
import requests

def quitar_espacios_iniciales(cadena):
    indice = 0
    for letra in cadena:
        if(letra == " "):
            indice += 1
        else:
            break
    return cadena[indice:]


link = "https://www.bookdepository.com/es/bestsellers"
response = requests.get(link)

html = response.content

soup = bs(html, "lxml")

## metodo find()

# print(soup.find("h2").get_text())
# soup.h1


## find_all()
# lista = soup.find_all("a")
# for elm in lista:
#     print(elm)


lista_titulos = soup.find_all("h3", class_="title")
lista_titulos_formato = []
for elemento in lista_titulos:
    lista_titulos_formato.append(elemento.get_text())

for i in range(len(lista_titulos_formato)):
    lista_titulos_formato[i] = lista_titulos_formato[i].replace("\n", "")
    lista_titulos_formato[i] = quitar_espacios_iniciales(lista_titulos_formato[i])


print(lista_titulos_formato)