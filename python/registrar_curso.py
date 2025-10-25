from almacenamiento_datos import cursos
from historial_cambios import agregar_cambio

def ejecutar():
    nombre = input("Nombre del curso: ").strip() # 
    if not nombre: 
        print("Nombre inválido")
        return
    try: 
        notaEnTexto = input("Nota del curso (0 a 100): ").strip() 
        nota = float(notaEnTexto) # 
    except ValueError:
        print("Nota inválida")
        return
    if nota < 0 or nota > 100: 
        print("La nota debe estar entre 0 y 100")
        return

    for c in cursos: 


        if c["nombre"].lower() == nombre.lower(): 
            print("El curso ya existe")
            return

    cursos.append({"nombre": nombre, "nota": nota}) # 

    agregar_cambio(f"Registrado curso: {nombre} con nota {nota}") 
    print("Curso registrado")
