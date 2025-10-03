from almacenamiento_datos import cursos
from historial_cambios import agregar_cambio

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    nombre = input("Nombre del curso a actualizar: ").strip()
    if not nombre:
        print("Nombre inválido")
        return
    indice = -1
    for i, c in enumerate(cursos):
        if c["nombre"].lower() == nombre.lower():
            indice = i
            break
    if indice == -1:
        print("Curso no encontrado")
        return
    try:
        nueva = float(input("Nueva nota (0 a 20): ").strip())
    except ValueError:
        print("Nota inválida")
        return
    if nueva < 0 or nueva > 20:
        print("La nota debe estar entre 0 y 20")
        return
    nota_anterior = cursos[indice]["nota"]
    cursos[indice]["nota"] = nueva
    agregar_cambio(f"Actualizada nota de {nombre}: {nota_anterior} -> {nueva}")
    print("Nota actualizada")
