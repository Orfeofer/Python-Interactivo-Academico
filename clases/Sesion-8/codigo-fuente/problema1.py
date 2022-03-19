class Raza:
    nombre = ""
    tipoRaza = ""
    nroObreros = -1
    nroRefinerias = -1
    mineral = -1
    gas = -1
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipoRaza = tipo
        self.nroObreros = 4
        self.nroRefinerias = 0
        self.mineral = 0
        self.gas = 0

    def __str__(self):
        return f"RECURSOS\nTipo de raza: {self.tipoRaza}\nNumero de obreros: {self.nroObreros}\nNumero de refinerias: {self.nroRefinerias}\nMineral: {self.mineral}\nGas: {self.gas}"
    
    def verRecursos(self):
        print("RECURSOS")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de raza: {self.tipoRaza}")
        print(f"Numero de obreros: {self.nroObreros}")
        print(f"Numero de refinerias: {self.nroRefinerias}")
        print(f"Mineral: {self.mineral}")
        print(f"Gas: {self.gas}")
    
    def produccion(self):
        self.mineral += self.nroObreros
        self.gas += 2*self.nroRefinerias
    
    def crearObrero(self):
        self.nroObreros += 1

    def crearRefineria(self):
        self.nroRefinerias += 1

criatura1 = Raza("Alex", "Protoss")

criatura1.verRecursos()