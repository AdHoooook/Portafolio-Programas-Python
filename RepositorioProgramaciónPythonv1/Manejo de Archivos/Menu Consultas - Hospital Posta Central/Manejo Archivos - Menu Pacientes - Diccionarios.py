
## SOLUCIÓN TRABAJO LENGUAJES DE PROGRAMACIÓN 2 USANDO DICCIONARIOS ##

## MANEJO INTERNO DE ARCHIVOS .TXT ##

##*******************************************************************##

## LIBRERIAS ADICIONALES NECESARIAS PARA RESOLVER EL PROBLEMA

##*******************************************************************##

from random import randint
import operator

##*******************************************************************##

## Función utilizada para leer el archivo de pacientes .TXT ## 

## COMPLETO ##
def leer_archivo_pacientes(validador):

    
    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt", "r") # Abrir el archivo en modo solo lectura y apuntar con *file
    
    file_ram = file.readlines() # Guardamos info.(imagen) de archivo en memoria

    file.close() # Cerramos archivo
    
    diccionario_pacientes = {} # Definición diccionario

    if validador == 1:
    
        for linea in file_ram:
                   
            info_paciente=linea.strip().split(';') # String
            info_final=[] # List or Array
        
            rut=info_paciente[0]
            nombre=info_paciente[1]
            edad=info_paciente[2]
            sexo=info_paciente[3]
            comuna=info_paciente[4]
            fono=info_paciente[5]
            prevision=info_paciente[6]
            isapre=info_paciente[7]
            fecha=info_paciente[8]
            ingreso=info_paciente[9]
            estado=info_paciente[10]

            info_final.append((nombre,edad,sexo,comuna,fono,prevision,isapre,fecha,ingreso,estado))
            diccionario_pacientes[rut]=info_final 
                                                    
                                                 
    if validador == 2:
    
        for linea in file_ram:
                
            info_paciente=linea.strip().split(';') # String
            info_final=[] # List or Array
        
            rut=info_paciente[0]
            nombre=info_paciente[1]
            edad=info_paciente[2]
            sexo=info_paciente[3]
            comuna=info_paciente[4]
            fono=info_paciente[5]
            prevision=info_paciente[6]
            isapre=info_paciente[7]
            fecha=info_paciente[8]
            ingreso=info_paciente[9]
            estado=info_paciente[10]

            info_final.append((rut,edad,sexo,comuna,fono,prevision,isapre,fecha,ingreso,estado))
            diccionario_pacientes[nombre]=info_final 
                                                     # Llenado de diccionario con 'Llave' [nombre]

    return(diccionario_pacientes) # Retorna diccionario al menú
                                  

## Función utilizada para modificar el archivo de pacientes .TXT ## 

## COMPLETO ## 
def modificar_archivo(rut_paciente, estado_paciente):

    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt", "r")

    file_ram = file.readlines() # Guardamos info.(imagen) de archivo en memoria

    file.close()

    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt", "w")

    string_mod = ""
    
    for linea in file_ram:

               
               
        if rut_paciente in linea:

            info_paciente=linea.strip().split(';') # String
                       
            rut=info_paciente[0]
            nombre=info_paciente[1]
            edad=info_paciente[2]
            sexo=info_paciente[3]
            comuna=info_paciente[4]
            fono=info_paciente[5]
            prevision=info_paciente[6]
            isapre=info_paciente[7]
            fecha=info_paciente[8]
            ingreso=info_paciente[9]
            estado=info_paciente[10]

            string_mod += (rut+";"+nombre+";"+edad+";"+sexo+";"+comuna+
                          ";"+fono+";"+prevision+";"+isapre+";"+fecha+
                          ";"+ingreso+";"+estado_paciente.upper()+"\n")

        if rut_paciente not in linea:

            string_mod += linea
                
    file.write(string_mod)
    file.close()
            
    # No retorna objeto alguno
    # Solamente sirve para modificar el archivo Pacientes2018.txt


## Función utilizada para generar nuevo archivo en orden de pacientes .TXT ## 

## COMPLETO ##
def generar_nuevo_archivo_pacientes_ordenados():

        
    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt","r")
    
    file_ram = file.readlines()
       
    diccionario_pacientes = {}

    lista_nuevo_orden = {}

    string_nuevo_diccionario = ""

    string_nuevo_orden = ""
    
    for linea in file_ram:

        info_paciente=linea.strip().split(';') # String
                    
        rut=info_paciente[0]
        nombre=info_paciente[1]
        edad=info_paciente[2]
        sexo=info_paciente[3]
        comuna=info_paciente[4]
        fono=info_paciente[5]
        prevision=info_paciente[6]
        isapre=info_paciente[7]
        fecha=info_paciente[8]
        ingreso=info_paciente[9]
        estado=info_paciente[10]

        string_nuevo_diccionario = (rut+";"+nombre+";"+edad+";"+sexo+";"+comuna+";"+fono+";"+prevision+";"+isapre+";"+fecha+";"+ingreso+";"+estado+"\n")           
        
        diccionario_pacientes[nombre] = string_nuevo_diccionario
      
    lista_nuevo_orden = sorted(diccionario_pacientes.items(), key=operator.itemgetter(0))

    for linea in lista_nuevo_orden:        

        string_nuevo_orden += linea[1]
                    
    new_file = open("C:/Users/Admin/Desktop/Pacientes2018_Nombres_Ordenados.txt", "w")
    new_file.write(string_nuevo_orden)

    
    file.close()
    new_file.close()
    
    # Sin retorno, sólo genera un nuevo archivo

## Función utilizada para generar nuevo archivo de pacientes hombres sin previsión .TXT ## 

## COMPLETO ##
def generar_nuevo_archivo_pacientes_hombres_sin_prevision():

        
    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt","r")
    
    file_ram = file.readlines()
       
    diccionario_pacientes = {}

    lista_nuevo_orden = {}

    string_nuevo_diccionario = ""

    string_nuevo_orden = ""
    
    for linea in file_ram:
        
        info_paciente=linea.strip().split(';') # String
                                
        rut=info_paciente[0]
        nombre=info_paciente[1]
        edad=info_paciente[2]
        sexo=info_paciente[3]
        comuna=info_paciente[4]
        fono=info_paciente[5]
        prevision=info_paciente[6]
        isapre=info_paciente[7]
        fecha=info_paciente[8]
        ingreso=info_paciente[9]
        estado=info_paciente[10]
        
        if sexo == 'M' and prevision == '4':
                       
            string_nuevo_diccionario = (rut+";"+nombre+";"+edad+";"+sexo+";"+comuna+";"+fono+";"+prevision+";"+isapre+";"+fecha+";"+ingreso+";"+estado+"\n")
            diccionario_pacientes[nombre] = string_nuevo_diccionario

         
    lista_nuevo_orden =  sorted(diccionario_pacientes.items(), key=operator.itemgetter(0))
    
    for linea in lista_nuevo_orden:        

        string_nuevo_orden += linea[1]
                    
    new_file = open("C:/Users/Admin/Desktop/Pacientes2018_Hombres_Sin_Prevision_Ordenados.txt", "w")
    new_file.write(string_nuevo_orden)
    
    file.close()
    new_file.close()

    # Sin retorno, sólo genera un nuevo archivo

## Función utilizada para generar nuevo archivo de ubicacion de pacientes .TXT ## 

## COMPLETO ##
def generar_nuevo_archivo_ubicacion_pacientes():
    
    file = open("C:/Users/Admin/Desktop/Pacientes2018.txt","r")
    
    file_ram = file.readlines()
       
    diccionario_pacientes = {}

    string_nueva_ubicacion = ""

    string_nuevo_archivo = ""
      
    for linea in file_ram:

        planta = str(randint(-2,6))
        habitacion = str(randint(0,200))
        
        info_paciente=linea.strip().split(';') # String
                                
        rut=info_paciente[0]
        nombre=info_paciente[1]
        edad=info_paciente[2]
        sexo=info_paciente[3]
        comuna=info_paciente[4]
        fono=info_paciente[5]
        prevision=info_paciente[6]
        isapre=info_paciente[7]
        fecha=info_paciente[8]
        ingreso=info_paciente[9]
        estado=info_paciente[10]
        
                       
        string_nueva_ubicacion = (rut+";"+nombre+";"+edad+";"+sexo+";"+comuna+";"+fono+";"+prevision+";"+isapre+";"+fecha+";"+ingreso+";"+estado+";"+planta+";"+habitacion+"\n")
        diccionario_pacientes[nombre] = string_nueva_ubicacion

    lista_nuevo_orden =  sorted(diccionario_pacientes.items(), key=operator.itemgetter(0))

    for linea in lista_nuevo_orden:        
        
        string_nuevo_archivo += linea[1]

                        
    new_file = open("C:/Users/Admin/Desktop/Pacientes2018_Ubicacion.txt", "w")
    new_file.write(string_nuevo_archivo)
    
    file.close()
    new_file.close()


## Función utilizada para leer el archivo de ubicación de pacientes .TXT ## 

## COMPLETO ##
def leer_archivo_ubicacion(validador):

    
    file = open("C:/Users/Admin/Desktop/Pacientes2018_Ubicacion.txt", "r") 
    
    file_ram = file.readlines() 

    file.close() 
    
    diccionario_ubicacion = {} 

    if validador == 1:
    
        for linea in file_ram:
                   
            info_paciente=linea.strip().split(';') # String
            info_final=[] # List or Array
        
            rut=info_paciente[0]
            nombre=info_paciente[1]
            edad=info_paciente[2]
            sexo=info_paciente[3]
            comuna=info_paciente[4]
            fono=info_paciente[5]
            prevision=info_paciente[6]
            isapre=info_paciente[7]
            fecha=info_paciente[8]
            ingreso=info_paciente[9]
            estado=info_paciente[10]
            planta=info_paciente[11]
            habitacion=info_paciente[12]

            info_final.append((nombre,edad,sexo,comuna,fono,prevision,isapre,fecha,ingreso,estado,planta,habitacion))
            diccionario_ubicacion[rut]=info_final # Llenado de diccionario
                                                  # con 'Llave' [rut]
                                                 
    if validador == 2:
    
        for linea in file_ram:
                
            info_paciente=linea.strip().split(';') # String
            info_final=[] # List or Array
        
            rut=info_paciente[0]
            nombre=info_paciente[1]
            edad=info_paciente[2]
            sexo=info_paciente[3]
            comuna=info_paciente[4]
            fono=info_paciente[5]
            prevision=info_paciente[6]
            isapre=info_paciente[7]
            fecha=info_paciente[8]
            ingreso=info_paciente[9]
            estado=info_paciente[10]
            planta=info_paciente[11]
            habitacion=info_paciente[12]

            info_final.append((rut,edad,sexo,comuna,fono,prevision,isapre,fecha,ingreso,estado,planta,habitacion))
            diccionario_ubicacion[nombre]=info_final # Llenado de diccionario
                                                     # con 'Llave' [nombre]

    return(diccionario_ubicacion) # Retorna diccionario con ubicaciones al menú



    
##****************************************************************##

## FUNCIONES PARA BUSCAR/CONSULTAR INFORMACIÓN DENTRO DE ARCHIVOS ##

##****************************************************************##

## Función que busca información del paciente según RUT ##

## COMPLETO ##           
def buscar_paciente_rut(diccionario_pacientes, rut_paciente):

    
    for linea in diccionario_pacientes:
        
        if rut_paciente in linea:

            for nombre, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado in diccionario_pacientes[rut_paciente]:

                                                
                string_retorno = ("\nLa información del paciente con rut: [" + rut_paciente + "] es:\n"+
                                  "\n[Rut]: " + rut_paciente + # Consultar profe: Como imprimir la llave 
                                  "\n[Nombre]: " + nombre +
                                  "\n[Edad]: " + edad +
                                  "\n[Sexo]: " + sexo +
                                  "\n[Comuna]: " + comuna +
                                  "\n[Fono]: " + fono +
                                  "\n[Prevision]: " + prevision +
                                  "\n[Nombre_Isapre]: " + isapre +
                                  "\n[Fecha]: " + fecha +
                                  "\n[Ingreso]: " + ingreso +
                                  "\n[Estado]: " + estado)
                return string_retorno


## Función que busca información del paciente según NOMBRE ##

## COMPLETO ##
def buscar_paciente_nombre(diccionario_pacientes, nombre_paciente):

    for linea in diccionario_pacientes:
                    
        if nombre_paciente.upper() in linea:

            for rut, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado in diccionario_pacientes[nombre_paciente.upper()]:

                                                
                string_retorno = ("\nLa información del paciente con nombre: [" + nombre_paciente.upper() + "] es:\n"+
                                  "\n[Rut]: " + rut +
                                  "\n[Nombre]: " + nombre_paciente.upper() +
                                  "\n[Edad]: " + edad +
                                  "\n[Sexo]: " + sexo +
                                  "\n[Comuna]: " + comuna +
                                  "\n[Fono]: " + fono +
                                  "\n[Prevision]: " + prevision +
                                  "\n[Nombre_Isapre]: " + isapre +
                                  "\n[Fecha]: " + fecha +
                                  "\n[Ingreso]: " + ingreso +
                                  "\n[Estado]: " + estado)
                return string_retorno 

## Función que consulta información sobre el diagnóstico de un paciente según RUT ## 

## COMPLETO ##
def consultar_diagnostico_ingreso(diccionario_pacientes, rut_paciente):

    for linea in diccionario_pacientes:

        if rut_paciente in linea:
                        
            for nombre, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado in diccionario_pacientes[rut_paciente]:

                                                
                string_retorno = ("\nEl diagnóstico de ingreso del paciente con rut: [" + rut_paciente + "] es:\n"+
                                   
                                  "\n[Nombre]: " + nombre +
                                  "\n[Ingreso]: " + ingreso)
                return string_retorno

## Función que consulta información sobre la ubicación de un paciente según RUT ## 

## COMPLETO ##
def ubicacion_paciente_rut(diccionario_ubicacion, rut_paciente):

    nueva_ubicacion = ""
   
    for lineas in diccionario_ubicacion:

        if rut_paciente in lineas:

            for nombre, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado, planta, habitacion in diccionario_ubicacion[rut_paciente]:
                
                nueva_ubicacion = ("\nEl paciente: ["+nombre+"] con rut: ["+rut_paciente+"] está ubicado en:"+
                                   
                                   "\n[Planta]: "+planta+ 
                                   "\n[Habitación]: "+habitacion+"\n")

    return nueva_ubicacion

## Función que consulta información sobre la ubicación de un paciente según NOMBRE ## 

## COMPLETO ##
def ubicacion_paciente_nombre(diccionario_ubicacion, nombre_paciente):
    
    nueva_ubicacion = ""
    
    for lineas in diccionario_ubicacion:

        if nombre_paciente.upper() in lineas:

            for rut, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado, planta, habitacion in diccionario_ubicacion[nombre_paciente.upper()]:

                nueva_ubicacion = ("\nEl paciente: ["+nombre_paciente.upper()+"] con rut: ["+rut+"] está ubicado en:"+
                                   
                                   "\n[Planta]: "+planta+ 
                                   "\n[Habitación]: "+habitacion+"\n")

    return nueva_ubicacion

## Función utilizada para actualizar/reemplazar el estado de un paciente según RUT ##

## COMPLETO ##
def cambiar_estado_paciente(diccionario_pacientes, rut_paciente, estado_paciente):

    for lineas in diccionario_pacientes:

        if rut_paciente in lineas:

            for nombre, edad, sexo, comuna, fono, prevision, isapre, fecha, ingreso, estado in diccionario_pacientes[rut_paciente]:

                if estado_paciente.upper() != estado:
                    string_retorno = ("\nSe ha cambiado el estado del paciente: [" + nombre + "] con rut: [" + rut_paciente+"]"+

                                      "\nAhora se encuentra en estado: [" + estado_paciente.upper()+"]")

                    modificar_archivo(rut_paciente, estado_paciente)
                    return string_retorno
                    
                elif estado_paciente.upper() == estado:
                    
                    string_retorno = ("\nEl paciente continua en estado"+' ['+ estado_paciente.upper()+"]")
                    return string_retorno
    

##*********************************************************************##

## FUNCIÓN "MENÚ DE CONSULTA" ##

##*********************************************************************##
                
def menu_consulta(opcion):

    # Consulta información de cualquier paciente
    if opcion == 1:

        print("\n")
        print("\n")
        print("Usted escogió mostrar información de un paciente")
        print("\n") 

               
        validador=int(input("Para buscar la infomación, marque [1]-rut o marque [2]-nombre:   "))
        diccionario_pacientes=leer_archivo_pacientes(validador)
        if validador == 1:
            
            rut_paciente=input("Ingrese el [rut] del paciente:   ")
            informacion_paciente=buscar_paciente_rut(diccionario_pacientes, rut_paciente)
            print(informacion_paciente)

            
        elif validador == 2:

            nombre_paciente=input("Ingrese el [nombre] del paciente:   ")
            informacion_paciente=buscar_paciente_nombre(diccionario_pacientes, nombre_paciente)
            print(informacion_paciente)

        elif validador !=1 and validador !=2:

            print("Las únicas opciones son 1 o 2")
            print("\n")
            print("\n")
       
                    
    # Consulta diagnóstico de ingreso de un paciente
    if opcion == 2:

        print("\n")
        print("\n")
        print("Usted escogió mostrar diagnóstico de ingreso de un paciente")
        print("\n")

        validador=1
        diccionario_pacientes=leer_archivo_pacientes(validador)
        rut_paciente=input("Para buscar la infomación, ingrese [rut] del paciente:  ")
        informacion_paciente=consultar_diagnostico_ingreso(diccionario_pacientes, rut_paciente)
        print(informacion_paciente)      
        
        print("\n")
        print("\n")
        
        
    # Muestra la ubicación de un paciente    
    if opcion == 3:

        print("\n")
        print("\n")
        print("Usted escogió mostrar ubicación de un paciente")
        print("\n")
        print("\n")

        validador=int(input("Para buscar la infomación, marque [1]-rut o [2]-nombre:    "))
        diccionario_ubicacion=leer_archivo_ubicacion(validador)

        if validador == 1:

            rut_paciente=input("Ingrese el [rut] del paciente:   ")
            informacion_paciente=ubicacion_paciente_rut(diccionario_ubicacion, rut_paciente)
            print(informacion_paciente)
            print("\n")
            print("\n")
            
        elif validador == 2:

            nombre_paciente=input("Ingrese el [nombre] del paciente:   ")
            informacion_paciente=ubicacion_paciente_nombre(diccionario_ubicacion, nombre_paciente)
            print(informacion_paciente)
            print("\n")
            print("\n")

        elif validador !=1 and validador !=2:

            print("Las únicas opciones son [1] ó [2]")
            print("\n")
            print("\n")
            

        
    # Cambia el estado actual de un paciente    
    if opcion == 4:

        print("\n")
        print("\n")
        print("Usted escogió cambiar el estado de un paciente")
        print("\n")
        print("\n")
        
        rut_paciente=input("Ingrese el [rut] del paciente:   ")
        estado_paciente=input("Ingrese el [estado actual] del paciente. [Leve, Medio, Grave]:   ")
        validador=1
        diccionario_pacientes=leer_archivo_pacientes(validador)
        if rut_paciente!= None:
            
            informacion_paciente=cambiar_estado_paciente(diccionario_pacientes, rut_paciente,estado_paciente)
            print(informacion_paciente)

    # Genera un nuevo archivo con los pacientes ordenados por nombre
    if opcion == 5:

        print("\n")
        print("\n")
        print("Usted escogió generar nuevo archivo [Pacientes ordenados por nombre]")
        print("\n")
        print("\n")
         
        generar_nuevo_archivo_pacientes_ordenados()
        print("\nNuevo archivo creado con éxito!")

    # Genera un nuevo archivo con los pacientes hombres sin prevision ordenados por nombre
    if opcion == 6:

        print("\n")
        print("\n")
        print("Usted escogió generar nuevo archivo [Pacientes Hombres sin Previsión ordenados por nombre]")
        print("\n")
        print("\n")

        generar_nuevo_archivo_pacientes_hombres_sin_prevision()
        print("\nNuevo archivo creado con éxito!")


        
##***************************************************************************##

## FUNCIÓN PRINCIPAL MAIN() ##

##***************************************************************************##


def main():
    omega=1
    print("\n")
    print("\n")
    generar_nuevo_archivo_ubicacion_pacientes()

    while omega!=0:
        print("\n")
        print("\n")
        print("Bienvenido al menu de consulta")
        print("Contamos con las siguientes opciones:")
        print("Opcion [1]: Mostrar información de un paciente")
        print("Opcion [2]: Mostrar diagnóstico de un paciente")
        print("Opcion [3]: Mostrar ubicación de un paciente")
        print("Opcion [4]: Cambiar estado de un paciente")
        print("Opcion [5]: Generar nuevo archivo [Pacientes ordenados por nombre]")
        print("Opcion [6]: Generar nuevo archivo [Pacientes Hombres sin previsión ordenados]")
        print("Opcion [7]: Salir del menú")
    
        opcion=int(input("Qué opción escoge?:  "))

        if opcion > 0 and opcion < 7:

            menu_consulta(opcion)
        
        elif opcion ==7:
            omega=0
            print("\n")
            print("\n")
            print("Usted escogió salir del menú")
            print("Hasta luego!")
            print("\n")
            
        else:

            print("\nError: Debe ingresar una de las opciones mencionadas...")
              
main()
