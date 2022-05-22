
## PROGRAMA CÁLCULADORA BÁSICA USANDO DIVERSAS FUNCIONES ##

import os
def cls():
    os.system('cls')

def sumar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)
    return suma

def multiplicar():
    valor1=int(input("Ingrese el primer numero entero:"))
    valor2=int(input("Ingrese el segundo numero entero:"))
    multi=valor1*valor2
    print("La multiplicacion da como resultado:",multi)
    return multi

def restar():
    valor1=int(input("Ingrese el primer numero entero"))
    valor2=int(input("Ingrese el segundo numero entero"))
    resta=valor1-valor2
    print("La diferencia es:",resta)
    return resta

def dividir():
    valor1=int(input("Ingrese el primer numero entero"))
    valor2=int(input("Ingrese el segundo numero entero"))
    division=valor1/valor2
    print("El resultado de la division es:",division)
    return division

def menu(opcion):

    if opcion==1:

        print("Usted eligio sumar")
        sumar()

    if opcion==2:

        print("Usted eligio restar")  
        restar()
    
    if opcion==3:

        print("Usted eligio multiplicar") 
        multiplicar()

    if opcion==4:

        print("Usted eligio dividir") 
        dividir()


### programa principal

print("**************************************")
print("Bienvenido a la calculadora de Phyton")
print("**************************************")
print("Si desea calcular sumas: Ingrese 1")
print("Si desea calcular restas: Ingrese 2")
print("Si desea calcular multiplicaciones: Ingrese 3")
print("Si desea calcular divisiones: Ingrese 4")
print("Si desea salir del programa: Ingrese 0")
print("**************************************")
opcion=int(input("Cual opcion elige?:"))
if opcion==0:
    print("Muchas gracias por utilizar nuestra calculadora")

while opcion!=0:

    menu(opcion)
    print("**************************************")
    print("Bienvenido a la calculadora de Phyton")
    print("**************************************")
    print("Si desea calcular sumas: Ingrese 1")
    print("Si desea calcular restas: Ingrese 2")
    print("Si desea calcular multiplicaciones: Ingrese 3")
    print("Si desea calcular divisiones: Ingrese 4")
    print("Si desea salir del programa: Ingrese 0")
    print("**************************************")
    opcion=int(input("Cual opcion elige?:"))
    if opcion==0:
        print("Muchas gracias por utilizar nuestra calculadora")
    

exit()
