
## PROGRAMA DE ENCRIPTACIÓN DE MENSAJE ENTRE SOCKETS CLIENTE-SERVIDOR ##

## CLIENTE ##

import socket

host="127.0.0.1"            
puerto=10000                

mi_socket=socket.socket()   
mi_socket.connect((host,puerto))

estado = True

while estado != False:

    # Enviar mensaje hacia Servidor

    mensaje_array = []
    mensaje_string=input("Ingrese el mensaje a enviar")
    string_final = ""

    i=0
    j=0
    while i < len(mensaje_string):
       
        mensaje_array.append(mensaje_string[i])

        i+=1



    if mensaje_string != "FIN" and "fin":

        x = 0

        while x < len(mensaje_array):

            if mensaje_array[x] == "A" or mensaje_array[x] == "a":

                mensaje_array[x] = "*"
            
            if mensaje_array[x] == "E" or mensaje_array[x] == "e":

                mensaje_array[x] = "-"
            
            if mensaje_array[x] == "I" or mensaje_array[x] == "i":

                mensaje_array[x] = "+"

            if mensaje_array[x] == "O" or mensaje_array[x] == "o":

                mensaje_array[x] = "#"

            if mensaje_array[x] == "U" or mensaje_array[x] == "u":

                mensaje_array[x] = "&"

            if mensaje_array[x] == "D" or mensaje_array[x] == "d":

                mensaje_array[x] = "¡"

            if mensaje_array[x] == "M" or mensaje_array[x] == "m":

                mensaje_array[x] = "¿"

            if mensaje_array[x] == "L" or mensaje_array[x] == "l":

                mensaje_array[x] = "="

            if mensaje_array[x] == "T" or mensaje_array[x] == "t":

                mensaje_array[x] = "?"

            if mensaje_array[x] == "P" or mensaje_array[x] == "p":

                mensaje_array[x] = "_"

            x = x + 1

        print(mensaje_array)

        while j < len(mensaje_array):
        
            string_final = string_final + str(mensaje_array[j])

            j+=1

                
        mi_socket.send(string_final.encode())

## Recibir mensaje de servidor
    
    data_cliente=mi_socket.recv(1024).decode()

    print(data_cliente)

    y=0
    z=0

    mensaje_array_cliente = []
    string_final_cliente = ""

    while y < len(data_cliente):

        mensaje_array_cliente.append(data_cliente[y])
        y+=1

    while z < len(mensaje_array_cliente):

        if mensaje_array_cliente[z] == "*":

            mensaje_array_cliente[z] = "A"

        if mensaje_array_cliente[z] == "-":

            mensaje_array_cliente[z] = "E"
        
        if mensaje_array_cliente[z] == "+":

            mensaje_array_cliente[z] = "I"

        if mensaje_array_cliente[z] == "#":

            mensaje_array_cliente[z] = "O"

        if mensaje_array_cliente[z] == "&":

            mensaje_array_cliente[z] = "U"

        if mensaje_array_cliente[z] == "¡":

            mensaje_array_cliente[z] = "D"

        if mensaje_array_cliente[z] == "¿":

            mensaje_array_cliente[z] = "M"

        if mensaje_array_cliente[z] == "=":

            mensaje_array_cliente[z] = "L"

        if mensaje_array_cliente[z] == "?":

            mensaje_array_cliente[z] = "T"

        if mensaje_array_cliente[z] == "_":

            mensaje_array_cliente[z] = "P"

        z = z + 1    


    print(mensaje_array_cliente)

    if mensaje_string == "FIN" or "fin":

        estado = False
            
mi_socket.close()                   
print("Comunicación terminada")
