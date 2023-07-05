class Persona:

    #---GETTERS---
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad
    
    #---SETTERS---
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido
 
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad

    #---ACCIONES---
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    


class Informatico(Persona):
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP"
        self.experiencia  = 5

    #---GETTERS---
    def getLenguajes(self):
        return self.lenguajes
    

    #--ACCIONES---
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def reparando(self):
        return "Estoy reparando"
    

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() #para acceder al constructor de Informático
        self.auditarRedes = "experto"
        self.experienciaRede = 15
    
    def auditoria(self):
        return "estoy auditando una red"