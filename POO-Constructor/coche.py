#Programación Orientada a Objetos (POO ó OOP)

#Definir una clase (molde para crear más objetos)
# Coche -> con características generales

class Coche:

    #Atributos, son propiedades
    color = "rojo"
    marca = "ferrari"
    modelo = "Aventador"
    caballaje = 300
    velocidad = 300
    plazas  = 2

    soy_publico = "soy, un atributo publico"

    __soy_privado = "soy un atributo privado"

    #Constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color  =color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #Métodos, son acciones

    #--Getter--
    def getPrivado(self):
        return self.__soy_privado
    
    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo
    
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "---- Información del coche ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info

    #--Setter--
    def setMarca(self, marca):
        self.marca = marca

    def setColor(self, color):
        self.color = color

    def setModelo(self, modelo):
        self.modelo = modelo

    #--Acciones
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -=1
    
    
    
    #fin defición clase

