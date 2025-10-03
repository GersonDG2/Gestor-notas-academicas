historial = []

def agregar_cambio(descripcion):
    historial.append(descripcion)

def ejecutar():
    if not historial:
        print("No hay cambios registrados en el historial")
        return
    print("Historial de cambios (más reciente primero):")
    for i in range(len(historial) - 1, -1, -1):
        print(f"{len(historial) - i}. {historial[i]}")
