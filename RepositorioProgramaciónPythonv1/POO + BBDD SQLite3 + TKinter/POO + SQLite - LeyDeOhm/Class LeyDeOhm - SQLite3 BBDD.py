
## PROGRAMA QUE ADMINISTRA BBDD CON SQLITE3 ##

## APLICATIVO PARA CALCULAR SEGÚN LEY DE OHM ##

import sqlite3

class LeyDeOHM:

    conexion = sqlite3.connect("OHM.db")        
 
     
    def __init__(self):
        
        print("===========")
       
        self.conexion.execute(""" create table if not exists LeyDeOHM(
                            id integer primary key AUTOINCREMENT,
                            voltaje integer,
                            intensidad integer,
                            resistencia integer
                    )""")
        print("Nueva Base de Datos creada!")
        self.conexion.commit()

    def cerrarConexion(self):

        self.conexion.commit()
        self.conexion.close()
                
    def calcularResistencia(self,distingue,voltaje,intensidad):

        self.distingue = distingue
        self.voltaje = voltaje
        self.intensidad = intensidad

        if self.intensidad == 0:
            
            print("No se puede calcular resistencia con intensidad = 0")
            
        elif self.intensidad != 0:
                   
            self.resistencia = self.voltaje / self.intensidad

        self.grabarCalculo(self.distingue,self.voltaje,self.intensidad,self.resistencia)
        return self.resistencia

    def calcularVoltaje(self,distingue,intensidad,resistencia):
        
        self.distingue = distingue
        self.intensidad = intensidad
        self.resistencia = resistencia

        self.voltaje = (self.intensidad*self.resistencia)

        self.grabarCalculo(distingue,self.intensidad,self.resistencia,self.voltaje)
        return self.voltaje

    def calcularIntensidad(self,distingue,voltaje,resistencia):
        
        self.distingue = distingue
        self.voltaje = voltaje
        self.resistencia = resistencia

        if resistencia == 0:
            
            print("No se puede calcular intensidad con resistencia = 0")
            
        elif resistencia != 0:
                   
            self.intensidad = (self.voltaje/self.resistencia)

        self.grabarCalculo(self.distingue,self.voltaje,self.resistencia,self.intensidad)
        return self.intensidad

    def grabarCalculo(self,distingue,varA,varB,resultado):

        if distingue == 1:

            self.conexion.execute(" insert into LeyDeOHM (voltaje,intensidad,resistencia) values (?,?,?)",
                            (varA,varB,resultado))
            self.conexion.commit()

            print("Los datos contenidos en la tabla OHM son los siguientes:")
            
            cursor = self.conexion.execute("select * from LeyDeOHM ")

            print("(ID,Voltaje,Intensidad,Resistencia)")
            
            for fila in cursor:

                print(fila)
            print("\n")

            

        if distingue == 2:

            self.conexion.execute(" insert into LeyDeOHM (voltaje,intensidad,resistencia) values (?,?,?)",
                            (resultado,varA,varB))
            self.conexion.commit()

            print("Los datos contenidos en la tabla OHM son los siguientes:")
            
            cursor = self.conexion.execute("select * from LeyDeOHM ")

            print("(ID,Voltaje,Intensidad,Resistencia)")

            for fila in cursor:
                
                print(fila)
            print("\n")

            self.conexion.close()

        if distingue == 3:

            self.conexion.execute(" insert into LeyDeOHM (voltaje,intensidad,resistencia) values (?,?,?)",
                            (varA,resultado,varB))
            self.conexion.commit()

            print("Los datos contenidos en la tabla OHM son los siguientes:")
            
            cursor = self.conexion.execute("select * from LeyDeOHM ")

            print("(ID,Voltaje,Intensidad,Resistencia)")
            
            for fila in cursor:

                print(fila)
            print("\n")

            self.conexion.close()



def menuConsultas(opcion):

    if opcion == 1:

        print("\n")
        print("\n")
        print("Usted escogió calcular la Resistencia...")
        print("\n")

        voltaje = int(input("Ingrese el voltaje: "))
        intensidad = int(input("Ingrese la intensidad: "))

        distingue=1
        ohm = LeyDeOHM()
        resistencia = ohm.calcularResistencia(distingue,voltaje,intensidad)
               
        print("La Resistencia estimada es: ", resistencia)
        print("=======================")
        print("\n")

    if opcion == 2:

        print("\n")
        print("\n")
        print("Usted escogió calcular el Voltaje...")
        print("\n")

        intensidad = int(input("Ingrese la intensidad: "))
        resistencia = int(input("Ingrese la resistencia: "))

        distingue=2
        ohm = LeyDeOHM()
        voltaje = ohm.calcularVoltaje(distingue,intensidad,resistencia)
         
        print("El Voltaje estimado es: ", voltaje)
        print("=======================")
        print("\n")

    if opcion == 3:

        print("\n")
        print("\n")
        print("Usted escogió calcular la Intensidad...")
        print("\n")

        voltaje = int(input("Ingrese el voltaje: "))
        resistencia = int(input("Ingrese la resistencia: "))

        distingue=3
        ohm = LeyDeOHM()
        intensidad = ohm.calcularIntensidad(distingue,voltaje,resistencia)
          
        print("La Intensidad estimada es: ", intensidad)
        print("=======================")
        print("\n")

    if opcion == 4:

        ohm = LeyDeOHM()
        ohm.cerrarConexion()
        
                

def main():   
    omega=1
    print("\n")
    print("\n")
    

    while omega!=0:
        
        print("Bienvenido al menu de consulta")
        print("========Ley_de_OHM============")
        print(" V = I x R ")
        print(" I = V / R ")
        print(" R = V / I ")
        print("==============================")
        print("Contamos con las siguientes opciones:")
        print("Opcion [1]: Calcular Resistencia")
        print("Opcion [2]: Calcular Voltaje")
        print("Opcion [3]: Calcular Intensidad")
        print("Opcion [4]: Salir del Menú")

        opcion = int(input("Qué opción escoge?:  "))

        if opcion > 0 and opcion < 4:

           menuConsultas(opcion)

        elif opcion == 4:

           menuConsultas(opcion)
           omega = 0
           print("\n")
           print("\n")
           print("Usted escogió salir del menú")
           print("Hasta luego!")
           print("\n")
            
        else:

           print("\nError: Debe ingresar una de las opciones mencionadas...")

main()
           
                
