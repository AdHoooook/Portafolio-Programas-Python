
## PROGRAMA UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS ##

class triangulo:

    def bautizar(self,lado1,lado2,lado3):

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):

        print("Los valores de los lados del triangulo son:")
        print("Lado1:",self.lado1)
        print("Lado2:",self.lado2)
        print("Lado3:",self.lado3)

    def mayor_lado(self):

        print("El lado más grande es:\n")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:

            print("Lado 1:",self.lado1)

        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:

            print("Lado 2:",self.lado2)

        else:

            print("Lado 3:",self.lado3)

    def tipo_triangulo(self):

        if self.lado1 == self.lado2 and self.lado1 == self.lado3:

            print("Es un triangulo equilatero")

        elif (self.lado1 == self.lado2 or self.lado1 == self.lado3) or (self.lado2 == self.lado1 or self.lado2 == self.lado3) or (self.lado3 == self.lado1 or self.lado3 == self.lado2):
            
            print("Es un triangulo isoseles")

        else:
            print("Es un triangulo escaleno") 

trianguloZ = triangulo()
trianguloZ.bautizar(9,88,2)
trianguloZ.mayor_lado()
trianguloZ.tipo_triangulo()

            

        
