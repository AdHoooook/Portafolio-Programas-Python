
## PROGRAMA QUE SUMA RECURSIVAMENTE LOS DÍGITOS DE UN NÚMERO DADO ##

def sumadig(num,numlen):

    if numlen <=0:
        return 0
    else:
        return int(num[numlen-1:numlen]) + sumadig(num,numlen-1)


while(True):
    num = input("Ingrese un numero positivo:")
    numlen = len(num)
    print(sumadig(num,numlen))

