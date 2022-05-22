
## PROGRAMA RECURSIVO SOBRE CÁLCULO DE FUNCIÓN FACTORIAL DE UN NÚMERO ## 

def factorial_recursiva(numero2):

    if numero2 == 1:

        return numero2
    
    else:

        return numero2 * factorial_recursiva(numero2-1)

x = 1

while x != 10:
    numero2 = int(input("ingrese un numero para realizar factorial: "))
    resultado2=int(factorial_recursiva(numero2))
    print(resultado2)
    x = int(input("Desea cerrar?? marque [10]: "))
    if x == 10:
        print("adioooooos....!")
    else:
        print("continuemos calculando...!")
