# modulo circunferencia.py

import math

def perimetro(radio):
	"""
	Función que calcula el perimetro de una circunferencia
	"""
	perimetro1 = 2 * math.pi * radio
	print ('El perimetro de la circunferencia con radio {0} es igual a {1}'.format(radio,perimetro1))
	return perimetro1

def area(radio):
	area1 = math.pi * radio ** 2
	print('El area de la circunferencia con radio {0} es igual a {1}'.format(radio,area1))
	return area1

def long_arco(radio):
	angulo = float(input('Ingresar el angulo en grados sexagesimales: '))
	angulo = (math.pi*angulo)/180

	longitud_de_arco = angulo*radio
	print('La longitud  de arco con radio {0} y angulo {1} es igual a {2}'.format(radio,angulo,longitud_de_arco))
	return longitud_de_arco

def area_sector_circular(radio):
	angulo = float(input('Ingresar el angulo en grados sexagesimales: '))
	angulo = (math.pi*angulo)/180
	return (0.5) * angulo * radio ** 2

def area_sector_circular_otro(lon_arc , radio):
	area1 = 0.5 * lon_arc * radio
	print("""El area del sector circular con :
	         longitud de arco = {0} y 
			 radio = {1} 
			 es = {2}""".format(lon_arc,radio, area1))