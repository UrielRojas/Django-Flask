from usuarios import usuario as user

from notas.acciones_notas import *

class Acciones:
    def registro(self):
        print("Registrate")
        nombre = input("Cuál es tu nombre?: ")
        apellidos = input("Cuál es tu apellido?: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")

        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] > 0:
            print("Usuario registrado")
        else:
            print("Registro incorrecto")

    def login(self):
        print("Indentifícate")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")

        usuario = user.Usuario('','',email,password)
        login = usuario.identificar()

        try:
            if email == login[3]:
                print(login)
                print("\nBienvendido al sistema")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        -crear notas
        -mostrar notas
        -eliminar
        -salir
        """)
        accion = input("Qué quieres hacer?: ")

        do = AccionesNotas()

        if accion == "crear":
            print("Crear")
            do.crear(usuario)
            self.proximasAcciones(usuario)
            

        elif accion == "mostrar":
            print("Tus notas")
            do.mostrar(usuario)
            self.proximasAcciones(usuario)


        elif accion == "eliminar":
            print("Nota eliminada")
            do.borrar(usuario)
            self.proximasAcciones(usuario)


        elif accion == "salir":
            print("Adiós")
            exit()
