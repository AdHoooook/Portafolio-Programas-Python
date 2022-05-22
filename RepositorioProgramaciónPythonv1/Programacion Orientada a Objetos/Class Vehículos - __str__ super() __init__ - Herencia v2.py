
## PROGRAMA UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS - HERENCIA ##

class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada)


class Camioneta(Auto):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada) 


def mostrar(vehiculos):
    for v in vehiculos:
        print(type(v).__name__, v)

lista = [
    Auto("rojo", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("azul", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

mostrar(lista)
