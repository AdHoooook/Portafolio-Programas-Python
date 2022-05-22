
## CÓDIGO EJEMPLIFICATIVO DONDE SE ITERA SOBRE DISTINTAS ESTRUCTURAS DE DATOS ##

# String para iterar
string_simple = '1234'

# String con parentesis
string_parentesis = ("1234")

# Lista de letras para iterar
lista_letras = ['uno','dos',"tres",'cuatro']


# Lista de números para iterar
lista_numerica = [1,2,3,4]


# Diccionario básico para iterar
diccionario = {
    "numero":"uno",
    "descripción": "primero"
}

# Diccionario anidado números para iterar
diccionario_anidado_0 = {
    "Numero Uno":{
        "numero": 1,
        "descripción": "primero"
    },
    "Numero Dos":{
        "numero": 2,
        "descripción": "segundo"
    },
    "Numero Tres":{
        "numero": 3,
        "descripción": "tercero"
    },
    "Numero Cuatro":{
        "numero": 4,
        "descripción": "cuarto"
    }
}


# Diccionario anidado letras para iterar
diccionario_anidado_1 = {
    "Numero Uno":{
        "numero": 'Uno',
        "descripción": "primero"
    },
    "Numero Dos":{
        "numero": 'Dos',
        "descripción": "segundo"
    },
    "Numero Tres":{
        "numero": 'Tres',
        "descripción": "tercero"
    },
    "Numero Cuatro":{
        "numero": "Cuatro",
        "descripción": "cuarto"
    }
}


for i in string_simple:
    print(i)

for i in string_parentesis:
    print(i)

for letra in lista_letras:
    print(letra)

for numero in lista_numerica:
    print(numero)


print(diccionario)
print("\n")
print("\n")



print(diccionario_anidado_0)
print("\n")

print("******FIJATE AQUI*******")

print(str(diccionario_anidado_0['Numero Uno']) + " - " + str(diccionario_anidado_0['Numero Dos']) + " - " + str(diccionario_anidado_0['Numero Tres']) + " - " + str(diccionario_anidado_0['Numero Cuatro']))
print("\n")
print("\n")
print(diccionario_anidado_0['Numero Uno']) 
print(diccionario_anidado_0['Numero Dos'])
print(diccionario_anidado_0['Numero Tres'])
print(diccionario_anidado_0['Numero Cuatro'])

print("\n")

print(diccionario_anidado_1)

for indice in diccionario_anidado_1:
    print(indice)

