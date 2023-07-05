from ConectorDB.mysqlConector import *
import datetime 

dbConexion = mysqlConnection()
dbCursor =  dbConexion.cursor()

class Nota:

    def __init__(self, usuario_id, titulo="", contenido=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.contenido = contenido


    def getUsuarioId(self):
        return self.usuario_id
    
    def getTitulo(self):
        return self.titulo
    
    def getContenido(self):
        return self.contenido

    def guardarNota(self):
        fecha= datetime.datetime.now()
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, %s)"

        nota = (self.getUsuarioId(), self.getTitulo(), self.getContenido(), fecha)
        
        dbCursor.execute(sql, nota)
        dbConexion.commit()

        return[dbCursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        dbCursor.execute(sql)

        result = dbCursor.fetchall()
        dbConexion.commit()

        return result
    
    def eliminir(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '{self.titulo}' "
        dbCursor.execute(sql)
        dbConexion.commit()

        return[dbCursor.rowcount, self]