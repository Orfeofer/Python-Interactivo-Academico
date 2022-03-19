from pandas.core.frame import DataFrame
from scrappingAutos import obtenerDatosAutos
import pandas as pd

class Auto:
    nombre = ""
    detalle = ""
    anio = 0
    precioDolares = 0
    ubicacion = ""
    def __init__(self, nombre, detalle, anio, precioDolares, ubicacion):
        self.nombre = nombre
        self.detalle = detalle
        self.anio = anio
        self.precioDolares = precioDolares
        self.ubicacion = ubicacion

    def exportarDiccionario(self):
        dic = {
            "nombre" : self.nombre,
            "detalle": self.detalle,
            "anio": self.anio,
            "precioDolares": self.precioDolares,
            "ubicacion": self.ubicacion
        }
        return dic

    def autoString(self):
        s = f"nombre: {self.nombre}\ndetalle: {self.detalle}\nanio: {self.anio}\nprecioDolares: {self.precioDolares}\nubicacion: {self.ubicacion}\n**************\n"
        return s

class DataAutos:
    listaAutos = []
    def __init__(self):
        self.listaAutos = []
    def __str__(self):
        s = ""
        for auto in self.listaAutos:
            s += auto.autoString()
        return s
    def agregarAuto(self, auto):
        self.listaAutos.append(auto)
    
    def exportarDataADataFrame(self):
        df = pd.DataFrame(diccionarioAutos)
        return df

diccionarioAutos = obtenerDatosAutos()

dataAutos = DataAutos()

for i in range(len(diccionarioAutos["nombre"])):
    auto = Auto(diccionarioAutos["nombre"][i], diccionarioAutos["detalles"][i], diccionarioAutos["anios"][i], diccionarioAutos["preciosDolares"][i], diccionarioAutos["ubicacion"][i])
    dataAutos.agregarAuto(auto)

dataFrame = dataAutos.exportarDataADataFrame()

print(dataFrame)