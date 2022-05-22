
class Caja:

    ancho = 0
    profundidad = 0
    alto = 0
    
    def __init__(self):

        self.ancho = int(input("Ingrese el ancho de la caja"))
        self.profundidad = int(input("Ingrese la profundidad de la caja"))
        self.alto = int(input("Ingrese el alto de la caja"))

        print("Nueva CAJA creada")

    def calcularVolumen(self):

        
        volumen = (self.ancho*self.profundidad*self.alto)
        return volumen

def main():

    
    omega = 1

    while(omega == 1):

        caja = Caja()
        volumenCaja = caja.calcularVolumen()
        print("El volumen de la caja es:", volumenCaja)
    


main()


    
    
