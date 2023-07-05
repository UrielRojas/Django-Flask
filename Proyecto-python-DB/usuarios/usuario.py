from ConectorDB.mysqlConector import *
import datetime
import hashlib

dbConexion = mysqlConnection()
dbCursor =  dbConexion.cursor()

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password

    def registrar(self):
        fecha= datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"

        #Crifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.getPassword().encode('utf8'))


        usuario = (self.getNombre(), self.getApellido(), self.getEmail(), cifrado.hexdigest(), fecha )

        
        try:
            dbCursor.execute(sql,usuario)
            dbConexion.commit()
            result = [dbConexion.rowcount, self]
        except:
            result = [0, self]

        dbCursor.close()
        dbConexion.close()

        return result

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.getEmail(), cifrado.hexdigest())
        dbCursor.execute(sql, usuario)

        result = dbCursor.fetchone()
        

        return result