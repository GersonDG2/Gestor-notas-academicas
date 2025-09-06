from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    aprobados = 0
    reprobados = 0
    for c in cursos:
        if c["nota"] >= 11:
            aprobados += 1
        else:
            reprobados += 1
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
