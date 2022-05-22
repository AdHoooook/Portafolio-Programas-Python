

## PROGRAMA QUE GENERA ARCHIVOS .TXT SOBRE CLIENTES DE UN CINE ##


def leer_archivo():

  
   #file = open("C:/Users/179578204/Desktop/bbd.txt", "r")

    file = open("C:/Users/Admin/Desktop/bbd.txt", "r")

    file_ram = file.readlines()

    file.close()

    return file_ram     # Retorna una lista con la información 


def escribir_archivo():

    archivo_revisar = leer_archivo()

    nuevo_string = ""

    for line in archivo_revisar:

        info_clientes = line.strip().split(';')

        if calcular_primo(info_clientes[0]) == "Es primo":

            nuevo_string = (nuevo_string + info_clientes[0] + ";" + info_clientes[1] + "," + "recibe Entrada" + "\n")
                        
        elif calcular_primo(info_clientes[0]) == "No es primo":

            nuevo_string = (nuevo_string + info_clientes[0] + ";" + info_clientes[1] + "," + "no recibe Entrada" + "\n")

    #archivo_nuevo = open("C:/Users/179578204/Desktop/descuento.txt", "w")
                
    archivo_nuevo = open("C:/Users/Admin/Desktop/descuento.txt", "w")

    archivo_nuevo.write(nuevo_string) # Ingresa la nueva información al archivo 

    archivo_nuevo.close()   
    
    print("Nuevo archivo generado: descuentos.txt")
        

def calcular_primo(rut_calc):
    
    i = 0
    j = 2
    suma = 0
    string_final="Es primo" # Sólo se retorna en caso de que la suma sea 1 o 2
                            # pues no entra al while j < suma
    
    while rut_calc[i]!= "-":           
        
        suma+=int(rut_calc[i])
        i = i+1
                    

    while j < suma:

        if suma%j == 0:

            string_final="No es primo"
            break

        elif suma%j != 0:

            string_final="Es primo"
            j = j+1
                    
    return string_final # Retorna un string que se usará para comparar en
                        # la función "Escribir_archivo()



print("Bienvenido a CineBlanet")

rut_calc= []
rut_calc=input("Ingrese un rut:")

print(calcular_primo(rut_calc))

escribir_archivo()


