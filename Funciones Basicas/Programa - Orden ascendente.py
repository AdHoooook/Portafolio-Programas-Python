
## PROGRAMACIÓN BÁSICA SOBRE ORDEN ASCENDENTE DE 3-N DÍGITOS

num1=input("Ingrese primer valor: ")
num1=int(num1)
num2=input("Ingrese segundo valor: ")
num2=int(num2)
num3=input("Ingrese tercer valor: ")
num3=int(num3)

if num1>num2 and num1>num3:
    max=num1
    elif num2<num3:
        min=num2
        med=num3
print("El orden ascendente de los números es: ", min,med,max)

if num2>num1 and num2>num3:
    max=num2
    elif num1<num3:
        min=num1
        med=num3
print("El orden ascendente de los números es: ", min,med,max)
    
if num3>num1 and num3>num2:
    max=num3
    elif num1<num2:
        min=num1
        med=num2
print("El orden ascendente de los números es: ", min,med,max)
    



