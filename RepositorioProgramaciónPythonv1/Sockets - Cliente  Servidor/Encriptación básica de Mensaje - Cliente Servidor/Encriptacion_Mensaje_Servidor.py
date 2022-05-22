
## PROGRAMA DE ENCRIPTACIÓN DE MENSAJE ENTRE SOCKETS CLIENTE-SERVIDOR ##

## SERVIDOR ##

import socket

host="127.0.0.1"    
puerto=10000        

mi_socket=socket.socket()
mi_socket.bind((host,puerto))
mi_socket.listen(1)     
conn,addr=mi_socket.accept() 

estado = True

while estado != False:

    # Recibir mensaje de Cliente
    
    data=conn.recv(1024).decode() 

    print(data)

    mensaje_array = []
    string_final = ""

    y=0
    z=0

    while y < len(data):

        mensaje_array.append(data[y])
        y+=1

    while z < len(mensaje_array):

        if mensaje_array[z] == "*":

            mensaje_array[z] = "A"

        if mensaje_array[z] == "-":

            mensaje_array[z] = "E"
        
        if mensaje_array[z] == "+":

            mensaje_array[z] = "I"

        if mensaje_array[z] == "#":

            mensaje_array[z] = "O"

        if mensaje_array[z] == "&":

            mensaje_array[z] = "U"

        if mensaje_array[z] == "¡":

            mensaje_array[z] = "D"

        if mensaje_array[z] == "¿":

            mensaje_array[z] = "M"

        if mensaje_array[z] == "=":

            mensaje_array[z] = "L"

        if mensaje_array[z] == "?":

            mensaje_array[z] = "T"

        if mensaje_array[z] == "_":

            mensaje_array[z] = "P"

        z = z + 1    


    print(mensaje_array)

    # Enviar mensaje a Cliente
    
    mensaje_array_servidor = []
    mensaje_string = input("Ingrese el mensaje a enviar")
    string_final = ""

    i=0
    j=0

    while i < len(mensaje_string):
       
        mensaje_array_servidor.append(mensaje_string[i])

        i+=1



    if mensaje_string != "FIN" and "fin":

        x = 0

        while x < len(mensaje_array_servidor):

            if mensaje_array_servidor[x] == "A" or mensaje_array_servidor[x] == "a":

                mensaje_array_servidor[x] = "*"
            
            if mensaje_array_servidor[x] == "E" or mensaje_array_servidor[x] == "e":

                mensaje_array_servidor[x] = "-"
            
            if mensaje_array_servidor[x] == "I" or mensaje_array_servidor[x] == "i":

                mensaje_array_servidor[x] = "+"

            if mensaje_array_servidor[x] == "O" or mensaje_array_servidor[x] == "o":

                mensaje_array_servidor[x] = "#"

            if mensaje_array_servidor[x] == "U" or mensaje_array_servidor[x] == "u":

                mensaje_array_servidor[x] = "&"

            if mensaje_array_servidor[x] == "D" or mensaje_array_servidor[x] == "d":

                mensaje_array_servidor[x] = "¡"

            if mensaje_array_servidor[x] == "M" or mensaje_array_servidor[x] == "m":

                mensaje_array_servidor[x] = "¿"
    
            if mensaje_array_servidor[x] == "L" or mensaje_array_servidor[x] == "l":

                mensaje_array_servidor[x] = "="

            if mensaje_array_servidor[x] == "T" or mensaje_array_servidor[x] == "t":

                mensaje_array_servidor[x] = "?"

            if mensaje_array_servidor[x] == "P" or mensaje_array_servidor[x] == "p":

                mensaje_array_servidor[x] = "_"

            x = x + 1

        print(mensaje_array_servidor)
    
        while j < len(mensaje_array_servidor):
                
            string_final = string_final + str(mensaje_array_servidor[j])

            j+=1

                          
        conn.send(string_final.encode())



    if mensaje_string == "FIN" or "fin":

        estado = False
    

mi_socket.close() 
print("Comunicación terminada")
