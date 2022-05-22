
## PROGRAMA UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS ##

class Cliente:

    def __init__(self, nombre):

        self.nombre=nombre
        self.monto=0


    def depositar(self, monto):

        self.monto=self.monto+monto

    def extraer(self, monto):

        self.monto=self.monto-monto

    def retornar_monto(self):

        return self.monto

    def imprimir(self):

        print(self.nombre,"tiene depositado la suma de: ",self.monto)


class Banco:

    def __init__(self):

        self.cliente1= Cliente("Ana")
        self.cliente2= Cliente("Juanizio")
        self.cliente3= Cliente("AdHok")

    def operar(self):

        self.cliente1.depositar(100)
        self.cliente2.depositar(200)
        self.cliente3.depositar(300)
        self.cliente3.extraer(150)

    def depositos_totales(self):

        total= self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print("El total del dinero del banco es: ",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()

        
            

        
