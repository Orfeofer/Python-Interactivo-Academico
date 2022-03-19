import random

def generarNroCuenta(listaCodigos):
    nroCuenta = ""
    for i in range(16):
        nroCuenta += str(random.randint(0, 9))
    
    if nroCuenta in listaCodigos:
        while nroCuenta in listaCodigos:
            nroCuenta = ""
            for i in range(16):
                nroCuenta += str(random.randint(0, 9))

    return nroCuenta

def es_moroso_str(es_moroso):
    if es_moroso:
        return "SI"
    else:
        return "NO"

def verificarMorosidad(cuentas):
    for cuenta in cuentas:
        if cuenta.saldo < 0:
            return True
    return False


class CuentaBancaria:
    nroCuenta = ""
    nombreBanco = ""
    saldo = 0
    def __init__(self, nroCuenta, nombreBanco):
        self.nroCuenta = nroCuenta
        self.nombreBanco = nombreBanco
        self.saldo = 0

    def verSaldo(self):
        print(f"Saldo actual de cuenta nro {self.nroCuenta} {self.nombreBanco}\nes: {self.saldo}")

    def abonar(self, monto):
        self.saldo += monto
    
    def pagar(self, monto):
        self.saldo -= monto

class Persona:
    dni = ""
    cuentas = []
    es_moroso = False

    def __init__(self, dni):
        self.dni = dni
        self.cuentas = []
        self.es_moroso = False
    
    def agregarCuenta(self, nombreBanco):
        nroCuentaNueva = generarNroCuenta(self.cuentas)
        cuentaNueva = CuentaBancaria(nroCuentaNueva, nombreBanco)
        self.cuentas.append(cuentaNueva)
    
    def quitarCuenta(self, nroCuenta):
        for i in range(len(self.cuentas)):
            if self.cuentas[i].nroCuenta == nroCuenta:
                self.cuentas.pop(i)
    
    def imprimirSaldos(self):
        self.es_moroso = verificarMorosidad(self.cuentas)
        estado_moroso = es_moroso_str(self.es_moroso)
        print(f"Es moroso: {estado_moroso}")
        for cuenta in self.cuentas:
            cuenta.verSaldo()
            print("###########################")

    def abonar(self, indice, cantidad):
        self.cuentas[indice].abonar(cantidad)

    def pagar(self, indice, cantidad):
        self.cuentas[indice].pagar(cantidad)


persona1 = Persona("82812315")
persona1.agregarCuenta("BCP")
persona1.agregarCuenta("Interbank")
persona1.agregarCuenta("BN")

persona1.imprimirSaldos()

persona1.abonar(0, 200)
persona1.abonar(1, 100)
persona1.abonar(2, 20)

persona1.pagar(2, 100)
print("\n\n")

persona1.imprimirSaldos()
