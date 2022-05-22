
## PROGRAMA CON LECTURA DE ARCHIVOS .TXT ##

# ORIGEN = datos.txt = [[45, 12, 98],[1,12,65],[7,15,76],[54,23,1],[65,2,84]] = 5x3 dimensiones


# Función que crea un archivo con un nombre escogido por usuario

def crear_archivo(nombre_archivo):

    archivo_creado = open("C:/Users/Admin/Desktop/"+nombre_archivo, "w")

    for i in range(0,20):

        archivo_creado.write(str(i) + "\r\n")

    archivo_creado.close()

# Función que suma los dígitos de cada línea del archivo original usando MATRICES

def suma_lineas(nombre_archivo):

    
    archivo_leido = open("C:/Users/Admin/Desktop/"+nombre_archivo, "r")
    A_leido = archivo_leido.readlines()
    linea_leidos = []
    lista_sumas = []    

        
    for linea in A_leido:
             

        linea_leidos = linea.split()
        valor1=int(linea_leidos[0])
        valor2=int(linea_leidos[1])
        valor3=int(linea_leidos[2])
        resultado=valor1+valor2+valor3
        lista_sumas.append(resultado)

    print(lista_sumas)
    archivo_leido.close()

# Función que suma los dígitos de cada columna del archivo original usando MATRICES

def suma_columnas(nombre_archivo):

    archivo_leido = open("C:/Users/Admin/Desktop/"+nombre_archivo, "r")
    A_leido = archivo_leido.readlines()
    linea_leidos = []
    lista_sumas = []

    columna1=0
    columna2=0
    columna3=0

    for linea in A_leido:

        linea_leidos = linea.split()
        columna1=int(columna1+int(linea_leidos[0]))
        columna2=int(columna2+int(linea_leidos[1]))
        columna3=int(columna3+int(linea_leidos[2]))

    lista_sumas.append(columna1)
    lista_sumas.append(columna2)
    lista_sumas.append(columna3)
    print(lista_sumas)
    archivo_leido.close()

# MAIN

crear_archivo("basile.txt")

suma_lineas("datos.txt")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

suma_columnas("datos.txt")




    







