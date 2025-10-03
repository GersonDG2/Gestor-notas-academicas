from almacenamiento_datos import cursos

cola_revisiones = []

def ejecutar():
    while True:
        print("\n--- Cola de Solicitudes de Revisión ---")
        print("1. Agregar solicitud de revisión")
        print("2. Atender siguiente solicitud")
        print("3. Ver cola de solicitudes")
        print("4. Volver al menú principal")
        op = input("Seleccione una opción: ").strip()
        
        if op == "1":
            if not cursos:
                print("No hay cursos registrados")
                continue
            nombre = input("Nombre del curso a revisar: ").strip()
            if not nombre:
                print("Nombre inválido")
                continue
            encontrado = False
            for c in cursos:
                if c["nombre"].lower() == nombre.lower():
                    encontrado = True
                    break
            if not encontrado:
                print("Curso no encontrado")
                continue
            cola_revisiones.append(nombre)
            print(f"Solicitud de revisión agregada para: {nombre}")
        
        elif op == "2":
            if not cola_revisiones:
                print("No hay solicitudes pendientes")
                continue
            atendido = cola_revisiones.pop(0)
            print(f"Atendiendo solicitud de: {atendido}")
        
        elif op == "3":
            if not cola_revisiones:
                print("No hay solicitudes pendientes")
                continue
            print("Solicitudes pendientes:")
            for i, sol in enumerate(cola_revisiones, 1):
                print(f"{i}. {sol}")
        
        elif op == "4":
            break
        
        else:
            print("Opción no válida")
