from almacenamiento_datos import cursos

def ejecutar():
    if not cursos:
        print("No hay cursos registrados")
        return
    
    cursos_ordenados = []
    for c in cursos:
        cursos_ordenados.append(c)
    
    n = len(cursos_ordenados)
    for i in range(1, n):
        clave = cursos_ordenados[i]
        j = i - 1
        while j >= 0 and cursos_ordenados[j]["nombre"].lower() > clave["nombre"].lower():
            cursos_ordenados[j + 1] = cursos_ordenados[j]
            j -= 1
        cursos_ordenados[j + 1] = clave
    
    nombre = input("Nombre del curso a buscar: ").strip()
    if not nombre:
        print("Nombre inválido")
        return
    
    nombre_buscar = nombre.lower()
    izquierda = 0
    derecha = len(cursos_ordenados) - 1
    encontrado = None
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = cursos_ordenados[medio]["nombre"].lower()
        
        if nombre_medio == nombre_buscar:
            encontrado = cursos_ordenados[medio]
            break
        elif nombre_medio < nombre_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    if encontrado is None:
        print("Curso no encontrado")
    else:
        print(f"Curso: {encontrado['nombre']} - Nota: {encontrado['nota']}")
