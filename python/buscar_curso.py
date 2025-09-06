from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    nombre = input("Nombre del curso a buscar: ").strip()
    if not nombre:
        print("Nombre inválido")
        return
    encontrado = None
    for c in cursos:
        if c["nombre"].lower() == nombre.lower():
            encontrado = c
            break
    if encontrado is None:
        print("Curso no encontrado")
    else:
        print(f"Curso: {encontrado['nombre']} - Nota: {encontrado['nota']}")
