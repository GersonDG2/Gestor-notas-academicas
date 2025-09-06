from almacenamiento_datos import cursos

def ejecutar():
    nombre = input("Nombre del curso: ").strip()
    if not nombre:
        print("Nombre inválido")
        return
    try:
        nota = float(input("Nota del curso (0 a 20): ").strip())
    except ValueError:
        print("Nota inválida")
        return
    if nota < 0 or nota > 20:
        print("La nota debe estar entre 0 y 20")
        return
    for c in cursos:
        if c["nombre"].lower() == nombre.lower():
            print("El curso ya existe")
            return
    cursos.append({"nombre": nombre, "nota": nota})
    print("Curso registrado")
