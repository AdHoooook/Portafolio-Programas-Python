
## PROGRAMA QUE UTILIZA LIBRERIAS SQLITE3 PARA GENERACIÓN Y CONEXIÓN CON BBDD ##

import sqlite3

conexion = sqlite3.connect("BasesDeDatosAlonso.db")


conexion.execute(""" create table YuGiOh(
                            id integer primary key AUTOINCREMENT,
                            nombre text,
                            fuerza integer
                    )""")

nombre=input("Ingrese el nombre de un personaje:")
fuerza=int(input("Ingrese la fuerza de ese personaje:"))

conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
                (nombre, fuerza))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Dama Oscura", 2000))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Espadachin de Llamas", 1400))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Dragon Blanco Ojos Azules", 3000))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Gaia el Caballero Feroz", 2300))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Obelisco el Atormentador", 4000))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Dragon Negro de Ojos Rojos", 2500))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Kuribo", 400))
#conexion.execute(" insert into YuGiOh (nombre,fuerza) values (?,?)",
#                ("Sagi El Payaso Oscuro", 1500))

conexion.commit()

cursor = conexion.execute("select * from YuGiOh ")

print("[Lista de Personajes de YuGiOh]")
print("*********************************")
      

for fila in cursor:

    print(fila)



print("***************************************************")
print("[Los Personajes con más de 2.400 de Fuerza son:]")


cursor2 = conexion.execute(" SELECT nombre,fuerza FROM YuGiOh WHERE fuerza > 2400 GROUP BY id ORDER BY fuerza DESC")

for fila2 in cursor2:

    print(fila2)

print("*******************************************************")
fuerza = int(input("Ingrese la fuerza de un Personaje:"))

cursor2 = conexion.execute(" SELECT id,nombre,fuerza FROM YuGiOh WHERE fuerza =?", (fuerza,))

fetchall = cursor2.fetchall()
if len(fetchall) > 0:
    for fila3 in fetchall:

        print(fila3)
else:
    print("No existe un personaje con aquella fuerza.")

conexion.close()


                
