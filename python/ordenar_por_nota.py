from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j]["nota"] > cursos[j + 1]["nota"]:
                temp = cursos[j]
                cursos[j] = cursos[j + 1]
                cursos[j + 1] = temp
    print("Cursos ordenados por nota (menor a mayor)")
    for i, c in enumerate(cursos, 1):
        print(f"{i}. {c['nombre']} - Nota: {c['nota']}")
