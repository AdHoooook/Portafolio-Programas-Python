
## PROGRAMA QUE ADMINISTRA BBDD CON SQLITE3 ##

## APLICATIVO PARA CALCULAR SEGÚN LEY DE OHM ##
                
import sqlite3

    
#"---------------calculo ley de ohm------------"
class LeyDeOHM:
    def __init__(self):
        self.v=0.0
        self.i=0.0
        self.r=0.0
        self.conexion=sqlite3.connect("OHM.db")
        self.conexion.execute("""create table if not exists tablaohm (codigo integer primary key AUTOINCREMENT,voltaje float,intensidad float,resistencia float)""")
        
    def resistencia(self,voltaje,intensidad):
                self.v=voltaje
                self.i=intensidad
                self.r=self.v/self.i
                self.grabar()
                return self.r
               
                 
    def voltaje(self,resistencia,intensidad):
                self.r=resistencia
                self.i=intensidad
                self.v=resistencia*intensidad
                self.grabar()
                return self.v

    def intensidad(self,voltaje,resistencia):
                self.v=voltaje
                self.r=resistencia
                self.i=voltaje/resistencia
                self.grabar()
                return self.i
            
    def grabar(self):
                self.conexion.execute("insert into tablaohm(voltaje,intensidad,resistencia) values (?,?,?)",(self.v,self.i,self.r))       
    def mostrar(self):
                cursor= self.conexion.execute("select codigo,voltaje,intensidad,resistencia from tablaohm")
                for fila in cursor:
                    print(fila)


    def cerrar(self):
        
                self.conexion.commit()
                self.conexion.close()
                     
                               
def menu():
        print("Ley de ohm")
        print("==========")
        print("          ")
        print("V = I x R ")
        print("I = V/R   ")
        print("R = V/I   ")
        print("          ")
        print("(1) Resistencia")
        print("(2) Voltaje")
        print("(3) Intensidad")
        print("(0) Salir")


#"------------programa principal-------------"

ohm=LeyDeOHM()

while(True): #ciclo infinito
    menu()
  
    opcion=input("ingrese opcion")
    if(opcion=="1"):
        while(True):
           try: 
                print("resistencia")
                v=float(input("ingrese voltaje:"))
                i=float(input("ingrese intensidad:"))
                r=ohm.resistencia(v,i)                  
                print("la resistencia es =",r,"ohm")
                break 
           except:
                print("el dato ingresado no es numerico")    
      
    elif(opcion=="2"):
        while(True):
            try:         
                print("voltaje")
                r=float(input("ingrese resistencia:"))
                i=float(input("ingrese intensidad:"))
                v= ohm.voltaje(r,i)                
                print("el voltaje es =",v,"v")
                break
            except:
                print("el dato ingresado no es numerico")  
                
    elif(opcion=="3"):
        while(True):
            try:     
                print("intensidad")
                v=float(input("ingrese voltaje:"))
                r=float(input("ingrese resistencia:"))
                i=ohm.intensidad(v,r)
                print("la intensida es =",i,"amp")
                break
            except:
                print("el dato ingresado no es numerico")   
    	
    elif(opcion=="0"):
                                  
    	break
    else:
    	print("opcion no corresponde")
print("Mostrando \n")
ohm.mostrar()
print("hasta pronto")
ohm.cerrar()
         

