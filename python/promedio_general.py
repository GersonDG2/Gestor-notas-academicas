from almacenamiento_datos import cursos

#Estructura esperada de cursos [{"nombre": "nombre del curso", "nota": nota del curso en numero}]

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    suma = 0
    for elementoActual in cursos:
        suma = suma + elementoActual["nota"]
    promedioGeneral = suma / len(cursos)
    print(f"Promedio general: {promedioGeneral:.2f}")
