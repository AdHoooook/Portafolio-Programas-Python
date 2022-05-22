
## PROGRAMA UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS ##

class Persona:
      
    def bautizar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

    def mayor_edad(self):

        if self.edad >=18:

            print("Es mayor de edad")
        else:

            print("Es menor de edad")

p1=Persona()
p1.bautizar("AdHok",27)
p1.imprimir()
p1.mayor_edad()

i = 1

while i != 0:


    print("\n")
    persona2_nombre = input("Nombre nueva persona: ")
    persona2_edad = int(input("Edad nueva persona: "))


    p2 = Persona()
    p2.bautizar(persona2_nombre, persona2_edad)
    p2.imprimir()
    p2.mayor_edad()

    print("Desea salir del Menú?")
    opcion = int(input("1 -> continuar     /   0 -> salir : "))
    
    i = opcion

print("Hasta luego!...")
