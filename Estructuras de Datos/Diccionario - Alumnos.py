#### PROGRAMA QUE CARGA ALUMNOS POR MEDIO DE RUT A UN DICCIONARIO.
#### LUEGO INGRESA MATERIAS CON SUS NOTAS

def cargar():
    alumnos={}
    for x in range(1):
        rut=int(input("Ingrese el numero de rut:"))
        listamaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese el nombre de materia que cursa:")
            nota=input("Ingrese la nota:")
            listamaterias.append((materia,nota))
            continua=input("Desea cargar otra materia para dicho alumno [s/n]:")
        alumnos[rut]=listamaterias
    return alumnos

def listar(alumnos):
    for rut in alumnos:
        print("rut del alumno:",rut)
        print("materias que cursa y notas:")
        for nota,materia in alumnos[rut]:
            print(materia,nota)

def consulta_notas(alumnos):
    rut=int(input("Ingrese el rut a consultar:"))
    if rut in alumnos:
        for materia,nota in alumnos[rut]:
            print(materia,nota)


alumnos=cargar()
consulta_notas(alumnos)
            
