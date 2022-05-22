
## PROGRAMA UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS - HERENCIA ##

class Vehiculo:

    lista_vehiculos = []
        
    def __init__(self):

        self.color=input("Ingrese el color del Vehiculo: ")
        self.ruedas=int(input("Ingrese la cantidad de ruedas del vehiculo: "))

    def mostrar_lista(self):

        for x in self.lista_vehiculos:
     
            print(x)

    def agregar_vehiculo(self, vehiculo):
              
            self.lista_vehiculos.append(vehiculo)
                      
class Automovil(Vehiculo):

    def __init__(self):

        super().__init__()
        self.velocidad=int(input("Ingrese la velocidad del automovil: "))
        self.cilindrada=int(input("Ingrese el cilindraje del automovil: "))

    def __str__(self):

        cadena = "Automovil(Color:"+self.color+","+str(self.ruedas)+" ruedas,"+str(self.velocidad)+" KM/H,"+str(self.cilindrada)+" cc)"
        return cadena

class Camioneta(Automovil):

    def __init__(self):

        super().__init__()
        self.carga=int(input("Ingrese la cantidad de carga que soporta la Camioneta: "))

    def __str__(self):

        cadena = "Camioneta(Color:"+self.color+","+str(self.ruedas)+" ruedas,"+str(self.velocidad)+"KM/H,"+str(self.cilindrada)+" cc,"+str(self.carga)+" KG)"
        return cadena

class Bicicleta(Vehiculo):

    def __init__(self):

        super().__init__()
        self.tipo=input("Es urbana o deportiva su Bicicleta/Motocicleta?: ")

    def __str__(self):

        cadena = "Bicicleta(Color:"+self.color+","+str(self.ruedas)+" ruedas,"+self.tipo+")"
        return cadena

class Motocicleta(Bicicleta):

    def __init__(self):

        super().__init__()
        self.velocidadM=int(input("Ingrese la velocidad de su Motocicleta: "))
        self.cilindradaM=int(input("Ingrese el cilindraje de su Motocicleta: "))

    def __str__(self):

        cadena = "Motocicleta(Color:"+self.color+","+str(self.ruedas)+" ruedas,"+self.tipo+","+str(self.velocidadM)+" KM/H,"+str(self.cilindradaM)+" cc)"
        return cadena
        


## Bloque principal


vehiculo1 = Automovil()
print("_________________________")
vehiculo2 = Camioneta()
print("_________________________")
vehiculo3 = Bicicleta()
print("_________________________")
vehiculo4 = Motocicleta()
print("_________________________")


vehiculo1.agregar_vehiculo(vehiculo1.__str__())
vehiculo2.agregar_vehiculo(vehiculo2.__str__())
vehiculo3.agregar_vehiculo(vehiculo3.__str__())
vehiculo4.agregar_vehiculo(vehiculo4.__str__())

vehiculo1.mostrar_lista()



            
