import sqlite3

#conexion

conexion = sqlite3.connect(".\Bases-datos\pruebas.db")

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+ 
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
               "titulo varchar(255), " +
               "descripcion text, "+
               "precio int(255)"+
               ")")

#Guardar cambios
conexion.commit()

#Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'ci','ci', 'ci')")
conexion.commit()

#listar datos

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print(productos)

for producto in productos:

    print("-----------------")
    print("ci: ",producto[1])
    print("ci: ",producto[2])
    print("ci: ",producto[3])
    


#Cerrar la conexión

conexion.close()