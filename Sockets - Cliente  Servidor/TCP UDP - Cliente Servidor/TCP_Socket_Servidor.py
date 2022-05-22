

## PROGRAMA SOCKET BÁSICO DE TRANSMISIÓN DE MENSAJE TCP CLIENTE-SERVIDOR ##

## SERVIDOR ##

import socket

host="127.0.0.1"    #DIRECION
puerto=10000        #PUERTO
mi_socket=socket.socket()#CONTRUCCTOR DEFAULT TCP
mi_socket.bind((host,puerto))#TUPLA 
mi_socket.listen(1)     #CANTIDAD DE CLIENTES
conn,addr=mi_socket.accept() #TUPLA QUE ACEPTA LA CONEXION
data=conn.recv(1024).decode() #RECIBE EL MENSAJE
print (data)
mi_socket.close() # CIERRA DEL SOCKET
