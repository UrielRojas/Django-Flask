from notas import nota as notes

class AccionesNotas:
    
    def crear(self, usuario):
        print(f"{usuario[1]}, Vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        contenido = input("introduce el contenido de tu nota: ")

        nota = notes.Nota(usuario[0], titulo, contenido)
        guardar = nota.guardarNota()

        print(guardar)
        if guardar[0] >0:
            print(f"Has guardado la nota: {nota.getTitulo()}")

        else:
            print("No se ha guardado la nota")

    def mostrar(self, usuario):
        print(f" {usuario[1]}, Aqui estan tus notas: ")
        nota = notes.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**************************************************************")
            print(f'''\t\tTitulo: {nota[2]}
                Contenido: {nota[3]}''')
            print("**************************************************************")

    def borrar(self, usuario):
        print(f" {usuario[1]}, vamos a borrar tu nota")

        titulo = input("Introduce el título de la nota a borrar: ")

        nota = notes.Nota(usuario[0], titulo)
        eliminar = nota.eliminir()

        if (eliminar[0]>0):
            print(f"Hemos eliminado la nota {nota.titulo}")

        else:
            print("Ocurrió algo inesperado, comprueba el nombre correcto de la nota a eliminar")