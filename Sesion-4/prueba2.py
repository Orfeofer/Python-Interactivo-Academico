import sys


#argv[1] recibe un entero e imprime un rango con ese valor

# sys.argv[1] = 3,  range(1,3) = [1,2]
for x in range(1,int(sys.argv[1])): 
    print(x)
    
# imprimir los argumentos pasados
print("Argumentos pasados:",sys.argv)