
## PROGRAMA QUE MANEJA ARCHIVOS Y GENERA MENÚ DE CONTACTOS ##

import os

CARPETA = 'C:/Users/Admin/Desktop/Prueba/'  #Carpeta donde se guardan contactos
EXTENSION = '.txt'                         #Extensión de archivos que guardan contactos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def crear_directorio():

    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    else:
        print("La carpeta ya existe")


def mostrar_menu():

    print("Seleccione del Menú lo que desea hacer:\r\n")
    print("1) Agregar nuevo contacto\r\n")
    print("2) Editar contacto\r\n")
    print("3) Ver contactos\r\n")
    print("4) Buscar contacto\r\n")
    print("5) Eliminar contacto\r\n")

def agregar_contacto():

    nombre_contacto = input("Nombre del contacto:\r\n")

    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:

            telefono_contacto = input("Agrega teléfono contacto:\r\n")
            categoria_contacto = input("Agrega categoria contacto:\r\n")

            #Instanciar objeto "Contacto"
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            print("\r\nContacto creado correctamente!")

    else: 
        print("Ese contacto ya existe...")
        
    #Reiniciar la App
    app_directorio()

def editar_contacto():

    nombre_anterior = input("Escribe el nombre de contacto a editar: \r\n")

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            nombre_contacto = input("Agregar nuevo nombre contacto:\r\n")
            telefono_contacto = input("Agrega nuevo teléfono contacto:\r\n")
            categoria_contacto = input("Agrega nueva categoria contacto:\r\n")

            #Instanciar objeto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            #Cerrar archivo editado, para finalizar editando el nombre de archivo del mismo
            archivo.close()

            #Renombrar archivo a editar
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
            #Mensaje éxito
            print("Edición realizada correctamente!")
    else:
        print("El contacto no existe")

def mostrar_contacto():


    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    print("Observación de contactos realizada con éxito!")

def buscar_contacto():

    nombre = input("Seleccione el contacto que desea buscar: \r\n")

    try:

        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\n Información del contacto:\r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("El archivo no existe")
        print(IOError)

    #Reiniciar App
    app_directorio()


def eliminar_contacto():

    nombre = input("Seleccione el contacto que desea eliminar: \r\n")

    try:
        os.remove(CARPETA + nombre + EXTENSION)    
        print("\r\nEliminado correctamente!")
    except expression as identifier:
        print("No existe el contacto...")

    #Reiniciar App
    app_directorio()        





def existe_contacto(nombre):

    return os.path.isfile(CARPETA + nombre + EXTENSION)


def app_directorio():

    #Revisa si la carpeta existe o no
    crear_directorio()


    #Invoca el menu de la app
    mostrar_menu()


    preguntar = True
    while preguntar:
        opcion = input("Selecciones una opción: \r\n")
        opcion = int(opcion)

        #Ejecutar las opciones

        if opcion == 1:
            print("Escogiste agregar un nuevo contacto")
            agregar_contacto()
            preguntar = False

        elif opcion == 2:
            print("Escogiste editar un contacto")
            editar_contacto()
            preguntar = False

        elif opcion == 3:
            print("Escogiste ver contactos")
            mostrar_contacto()
            preguntar = False

        elif opcion == 4:
            print("Escogiste buscar un contacto")
            buscar_contacto()
            preguntar = False

        elif opcion == 5:
            print("Escogiste eliminar un contacto")
            eliminar_contacto()
            preguntar = False




#Llamado a la función que levanta la app
app_directorio()










