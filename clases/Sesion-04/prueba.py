import sys
#sys.argv simplemente es una lista que contiene los argumentos posicionales
#arguments python prueba.py (alumnos 2021)
#sys.argv = [nombre_programa, argumento1, argumento2  ]

print("Hola {}. Bienvenido al curso de Python {}".format(sys.argv[1], sys.argv[2]))

print("estos son los argumentos pasados: ",sys.argv)