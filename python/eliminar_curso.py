from almacenamiento_datos import cursos
from historial_cambios import agregar_cambio

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
            nota_eliminada = c["nota"]
            del cursos[i]
            agregar_cambio(f"Eliminado curso: {nombre} (nota: {nota_eliminada})")
            print("Curso eliminado")
            return
    print("Curso no encontrado")
