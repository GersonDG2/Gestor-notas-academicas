from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    s = 0
    for c in cursos:
        s += c["nota"]
    p = s / len(cursos)
    print(f"Promedio general: {p:.2f}")
