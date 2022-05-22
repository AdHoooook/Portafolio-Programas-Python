
## PROGRAMA DE FUNCIÓN RECURSIVA QUE SIRVE PARA DIVIDIR NÚMEROS ##

def division(dividendo,divisor):
    if dividendo<divisor:
        return 0
    else:
        
        return 1 + division(dividendo-divisor,divisor)


print(division(16,2))
