from usuarios import acciones

Do = acciones.Acciones()

print(
    """ 
    Acciones Disponibles
        -registro
        -login
    """
)

accion = input("Qué quieres hacer: ")

if accion == "registro":
    Do.registro()


elif accion == "login":
    Do.login()
    