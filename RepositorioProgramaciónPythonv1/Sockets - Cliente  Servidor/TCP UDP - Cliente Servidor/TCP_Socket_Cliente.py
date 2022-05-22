
## PROGRAMA SOCKET BÁSICO DE TRANSMISIÓN DE MENSAJE TCP CLIENTE-SERVIDOR ##

## CLIENTE ##

import socket

host="127.0.0.1"            #HOST
puerto=10000                #PUERTO

mi_socket=socket.socket()   #CONTRUCCION DEFAULT TCP
mi_socket.connect((host,puerto))    #TUPLA DE CONEXION

mensaje="HOLA, CÓMO ESTÁS"
mi_socket.send(mensaje.encode())    #MENSAJE ENVIADO
mi_socket.close()                   #CIERRE DEL SOCKET
