from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    n = len(cursos)
    for i in range(1, n):
        clave = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]["nombre"].lower() > clave["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = clave
    print("Cursos ordenados alfabéticamente por nombre:")
    for i, c in enumerate(cursos, 1):
        print(f"{i}. {c['nombre']} - Nota: {c['nota']}")
