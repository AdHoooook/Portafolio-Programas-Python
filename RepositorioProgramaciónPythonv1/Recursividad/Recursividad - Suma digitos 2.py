
## PROGRAMA QUE SUMA RECURSIVAMENTE LOS DÍGITOS DE UN NÚMERO V2 ##

def sumadig2(num):
    if num==0:
        return 0

    else:

        return (num%10) + sumadig2(num//10)


while(True):
    num = int(input("Ingrese un numero positivo:"))
    print(sumadig2(num))


