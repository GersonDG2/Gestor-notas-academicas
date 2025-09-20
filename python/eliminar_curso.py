from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    nombre = input("Nombre del curso a eliminar: ").strip()
    if not nombre:
        print("Nombre inválido")
        return
    for i, c in enumerate(cursos):
        if c["nombre"].lower() == nombre.lower():
            del cursos[i]
            print("Curso eliminado")
            return
    print("Curso no encontrado")
