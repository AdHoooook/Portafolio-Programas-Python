
## PROGRAMA DE EJEMPLO UTILIZACIÓN FRAMEWORK PYMYSQL - BBDD MYSQL ##


import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=1521,
                             user='SYSTEM',
                             password='adhok',
                             db='BDDAdHok',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
        # Insert Data
        cursor = connection.cursor()
        sql = "INSERT INTO `planetas` VALUES ('marte','rojo')"
        cursor.execute(sql)
        connection.commit()       
    
        # Read a single record
        cursor = connection.cursor()
        sql = "SELECT * from 'planetas'"        
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        
finally:
    connection.close()
