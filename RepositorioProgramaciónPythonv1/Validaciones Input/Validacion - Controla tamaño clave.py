i = 1
while i != 0:
    clave = input("Ingrese una clave, por favor: ")
    if len(clave) >= 10 and len(clave)<= 20:
        print("La clave es válida")
    else:
        print("Error en la clave: Verifique que su clave contiene entre 10 y 20 caracteres")
        i = 0