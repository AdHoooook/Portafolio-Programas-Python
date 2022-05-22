
## MATRICES ##



matriz=[]
filas=3
columnas=4
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(0)
print("Matriz")
print(matriz)



matriz2=[]
filas=5
columnas=5
matriz2=[None]*filas
for i in range(filas):
    matriz2[i]=[0]*columnas
print("Matriz2")
print(matriz2)


matriz3=[]
filas=2
columnas=3
matriz3=[[0]*columnas for i in range(filas)]
print("Matriz3")
print(matriz3)


dimension=int(input("Ingrese dimension:"))
unidad=[]
for i in range(dimension):
    unidad.append([])
    for j in range(dimension):
        if j==i:
            unidad[i].append(1)
        else:
            unidad[i].append(0)

print(unidad) 
