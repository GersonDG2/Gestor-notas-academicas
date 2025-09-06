from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    print("Listado de cursos:")
    for i, c in enumerate(cursos, 1):
        print(f"{i}. {c['nombre']} - Nota: {c['nota']}")
