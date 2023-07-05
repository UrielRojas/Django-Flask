import clases

persona  = clases.Persona()

persona.setNombre("Uriel")
persona.setApellido("Rojas")
persona.setAltura("178cm")
persona.setEdad("24 años")


print(f"La persona es: {persona.getNombre()}  {persona.getApellido()}")
print(persona.hablar())
print("------------------------------------------------------------------")

informatico = clases.Informatico()

informatico.setNombre("Kevin")
informatico.setApellido("Iacovelli")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("------------------------------------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Bely")

print(tecnico.getNombre(), tecnico.getLenguajes())