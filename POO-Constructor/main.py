from coche import Coche

carro  = Coche("Amarillo", "Renault","Clio", 150, 200, 4)
carro1  = Coche("Verde", "Renault","Clio", 240, 200, 4)
carro2  = Coche("Rojas", "Renault","Clio", 150, 200, 4)
carro3  = Coche("Azul", "Renault","Clio", 350, 200, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

#Visibilidad
print(carro.soy_publico)
print(carro.getPrivado())