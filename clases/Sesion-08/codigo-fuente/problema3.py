class Casa_t:
    direccion = ""
    x = 0
    y = 0

    def __init__(self, direccion, x, y):
        self.direccion = direccion
        self.x = x
        self.y = y
    
    def get_direccion(self):
        return self.direccion
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_distancia(self, x2, y2):
        d = (x2-self.x)**2 + (y2-self.y)**2
        d = d**(0.5)
        return d


n = int(input())
lista_casas = []

for i in range(n):
    direccion = input()
    posicion = input().split(" ")
    x = int(posicion[0])
    y = int(posicion[1])

    casa = Casa_t(direccion, x, y)
    lista_casas.append(casa)

posicion = input().split(" ")
x = int(posicion[0])
y = int(posicion[1])

indice = 0
distancia_minima = 1000000000

for i in range(len(lista_casas)):
    if distancia_minima > lista_casas[i].get_distancia(x, y):
        distancia_minima = lista_casas[i].get_distancia(x, y)
        indice = i

print(f"direccion = {lista_casas[indice].direccion}")
print(f"distancia = {distancia_minima}")