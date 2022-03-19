def area(tipo_poligono):

	if tipo_poligono == 'cuadrado':
		lado = float(input('Ingresa el lado del cuadrado: '))
		area = lado ** 2
		print('El area del cuadrado con lado = {0} es {1}'.format(lado,area))
	
	return area

#def perimetro(tipo_poligono):




