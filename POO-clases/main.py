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

    #Métodos, son acciones

    #--Getter--

    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo
    
    def getVelocidad(self):
        return self.velocidad

    #--Setter--
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

print("--COCHE UNO--")
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("Murciélago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print ("Velocidad nueva: ", coche.getVelocidad())


##Crrear más objetos
print("--COCHE Dos--")

coche2 = Coche()
coche2.setColor("verde") 
coche2.setModelo("Gallardo")
print(coche2.marca,coche2.getModelo(), coche2.getColor())

