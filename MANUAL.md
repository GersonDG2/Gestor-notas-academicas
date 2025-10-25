# MANUAL DE USUARIO
## Gestor de Notas Académicas

---

## Tabla de Contenidos

1. Introducción
2. Requisitos del Sistema
3. Cómo Ejecutar el Programa
4. Menú Principal
5. Descripción de Funcionalidades
6. Ejemplos de Uso

---

## 1. Introducción

El Gestor de Notas Académicas es un programa de consola desarrollado en Python que permite a los estudiantes registrar, consultar y gestionar las calificaciones de sus cursos de manera sencilla y eficiente.

**Características principales:**
- Registro de cursos con sus respectivas notas
- Cálculo automático de promedios
- Búsqueda de cursos (lineal y binaria)
- Ordenamiento de cursos por nota o nombre
- Historial de cambios realizados
- Sistema de cola para solicitudes de revisión

---

## 2. Requisitos del Sistema

**Software necesario:**
- Python 3.x instalado en el sistema
- Sistema operativo: Windows, Linux o macOS
- Terminal o consola de comandos

**Conocimientos requeridos:**
- Uso básico de la terminal
- Comprensión de conceptos de calificaciones académicas

---

## 3. Cómo Ejecutar el Programa

**Paso 1:** Abrir la terminal o consola de comandos

**Paso 2:** Navegar hasta la carpeta del proyecto
```
cd ruta/a/Gestor-notas-academicas/python
```

**Paso 3:** Ejecutar el programa
```
python menu.py
```

**Paso 4:** El menú principal se mostrará en pantalla y estará listo para recibir comandos

---

## 4. Menú Principal

Al ejecutar el programa, verá el siguiente menú:

```
====== GESTOR DE NOTAS ACADÉMICAS ======
1. Registrar nuevo curso
2. Mostrar todos los cursos y notas
3. Calcular promedio general
4. Contar cursos aprobados y reprobados
5. Buscar curso por nombre (búsqueda lineal)
6. Actualizar nota de un curso
7. Eliminar un curso
8. Ordenar cursos por nota (burbuja)
9. Ordenar cursos por nombre (inserción)
10. Buscar curso por nombre (búsqueda binaria)
11. Simular cola de solicitudes de revisión
12. Mostrar historial de cambios (pila)
13. Salir
```

**Para seleccionar una opción:** Ingrese el número correspondiente y presione Enter.

---

## 5. Descripción de Funcionalidades

### 5.1 Registrar Nuevo Curso (Opción 1)

**Descripción:**
Permite agregar un nuevo curso al sistema con su respectiva calificación.

**Datos de entrada:**
- Nombre del curso (texto)
- Nota del curso (número entre 0 y 100)

**Validaciones:**
- El nombre no puede estar vacío
- La nota debe ser un número válido
- La nota debe estar en el rango de 0 a 100
- No se pueden registrar cursos duplicados (mismo nombre)

**Ejemplo de uso:**
```
Seleccione una opción: 1
Nombre del curso: Matemáticas
Nota del curso (0 a 100): 85
Curso registrado
```

**Salida esperada:**
- Mensaje de confirmación: "Curso registrado"
- El curso se agrega al historial de cambios

**Posibles errores:**
- "Nombre inválido" - si no ingresa un nombre
- "Nota inválida" - si ingresa texto en lugar de número
- "La nota debe estar entre 0 y 100" - si la nota está fuera del rango
- "El curso ya existe" - si intenta registrar un curso duplicado

---

### 5.2 Mostrar Todos los Cursos y Notas (Opción 2)

**Descripción:**
Muestra una lista completa de todos los cursos registrados con sus respectivas notas.

**Datos de entrada:**
Ninguno

**Ejemplo de uso:**
```
Seleccione una opción: 2
Listado de cursos:
1. Matemáticas - Nota: 85.0
2. Historia - Nota: 70.0
3. Física - Nota: 92.5
```

**Salida esperada:**
- Lista numerada con formato: "Número. Nombre - Nota: valor"
- Si no hay cursos: "No hay cursos registrados"

---

### 5.3 Calcular Promedio General (Opción 3)

**Descripción:**
Calcula y muestra el promedio aritmético de todas las notas registradas.

**Datos de entrada:**
Ninguno

**Fórmula utilizada:**
```
Promedio = Suma de todas las notas / Cantidad de cursos
```

**Ejemplo de uso:**
```
Seleccione una opción: 3
Promedio general: 82.5
```

**Salida esperada:**
- Promedio con decimales
- Si no hay cursos: "No hay cursos registrados"

---

### 5.4 Contar Cursos Aprobados y Reprobados (Opción 4)

**Descripción:**
Cuenta y muestra cuántos cursos están aprobados y cuántos reprobados según el criterio de aprobación.

**Criterio de aprobación:**
- Aprobado: nota mayor o igual a 60
- Reprobado: nota menor a 60

**Datos de entrada:**
Ninguno

**Ejemplo de uso:**
```
Seleccione una opción: 4
Cursos aprobados: 2
Cursos reprobados: 1
```

**Salida esperada:**
- Cantidad de cursos aprobados
- Cantidad de cursos reprobados
- Si no hay cursos: "No hay cursos registrados"

---

### 5.5 Buscar Curso por Nombre - Búsqueda Lineal (Opción 5)

**Descripción:**
Busca un curso específico en la lista utilizando el algoritmo de búsqueda lineal (secuencial).

**Datos de entrada:**
- Nombre del curso a buscar (texto)

**Características:**
- No requiere que la lista esté ordenada
- Búsqueda no sensible a mayúsculas/minúsculas
- Recorre la lista de inicio a fin

**Ejemplo de uso:**
```
Seleccione una opción: 5
Nombre del curso a buscar: matemáticas
Curso: Matemáticas - Nota: 85.0
```

**Salida esperada:**
- Información del curso encontrado (nombre y nota)
- Si no existe: "Curso no encontrado"
- Si el nombre está vacío: "Nombre inválido"

---

### 5.6 Actualizar Nota de un Curso (Opción 6)

**Descripción:**
Modifica la calificación de un curso ya registrado en el sistema.

**Datos de entrada:**
- Nombre del curso a actualizar (texto)
- Nueva nota (número entre 0 y 100)

**Validaciones:**
- El curso debe existir en el sistema
- La nueva nota debe ser un número válido
- La nueva nota debe estar entre 0 y 100

**Ejemplo de uso:**
```
Seleccione una opción: 6
Nombre del curso a actualizar: Historia
Nueva nota (0 a 100): 75
Nota actualizada
```

**Salida esperada:**
- Mensaje de confirmación: "Nota actualizada"
- El cambio se registra en el historial

**Posibles errores:**
- "No hay cursos registrados" - si la lista está vacía
- "Nombre inválido" - si no ingresa un nombre
- "Curso no encontrado" - si el curso no existe
- "Nota inválida" - si ingresa texto en lugar de número
- "La nota debe estar entre 0 y 100" - si está fuera del rango

---

### 5.7 Eliminar un Curso (Opción 7)

**Descripción:**
Borra permanentemente un curso del sistema.

**Datos de entrada:**
- Nombre del curso a eliminar (texto)

**Advertencia:** Esta acción no se puede deshacer. El curso se eliminará permanentemente.

**Validaciones:**
- El curso debe existir en el sistema
- El nombre no puede estar vacío

**Ejemplo de uso:**
```
Seleccione una opción: 7
Nombre del curso a eliminar: Física
Curso eliminado
```

**Salida esperada:**
- Mensaje de confirmación: "Curso eliminado"
- El cambio se registra en el historial

**Posibles errores:**
- "No hay cursos registrados" - si la lista está vacía
- "Nombre inválido" - si no ingresa un nombre
- "Curso no encontrado" - si el curso no existe

---

### 5.8 Ordenar Cursos por Nota (Opción 8)

**Descripción:**
Ordena la lista de cursos de menor a mayor nota utilizando el algoritmo de ordenamiento burbuja.

**Datos de entrada:**
Ninguno

**Características:**
- Algoritmo utilizado: Burbuja (Bubble Sort)
- Orden: Ascendente (de menor a mayor)
- Modifica el orden permanente de la lista

**Ejemplo de uso:**
```
Seleccione una opción: 8
Cursos ordenados por nota (menor a mayor)
1. Historia - Nota: 70.0
2. Matemáticas - Nota: 85.0
3. Física - Nota: 92.5
```

**Salida esperada:**
- Mensaje de confirmación
- Lista ordenada de cursos con sus notas
- Si no hay cursos: "No hay cursos registrados"

---

### 5.9 Ordenar Cursos por Nombre (Opción 9)

**Descripción:**
Ordena la lista de cursos alfabéticamente por nombre utilizando el algoritmo de ordenamiento por inserción.

**Datos de entrada:**
Ninguno

**Características:**
- Algoritmo utilizado: Inserción (Insertion Sort)
- Orden: Alfabético (A-Z)
- No sensible a mayúsculas/minúsculas
- Modifica el orden permanente de la lista

**Ejemplo de uso:**
```
Seleccione una opción: 9
Cursos ordenados alfabéticamente por nombre:
1. Física - Nota: 92.5
2. Historia - Nota: 70.0
3. Matemáticas - Nota: 85.0
```

**Salida esperada:**
- Mensaje de confirmación
- Lista ordenada alfabéticamente
- Si no hay cursos: "No hay cursos registrados"

---

### 5.10 Buscar Curso por Nombre - Búsqueda Binaria (Opción 10)

**Descripción:**
Busca un curso específico utilizando el algoritmo de búsqueda binaria, que es más eficiente para listas grandes.

**Datos de entrada:**
- Nombre del curso a buscar (texto)

**Características:**
- Algoritmo utilizado: Búsqueda binaria
- Ordena automáticamente una copia de la lista antes de buscar
- No modifica el orden original de los cursos
- Búsqueda no sensible a mayúsculas/minúsculas
- Más eficiente que la búsqueda lineal

**Ejemplo de uso:**
```
Seleccione una opción: 10
Nombre del curso a buscar: Historia
Curso: Historia - Nota: 70.0
```

**Salida esperada:**
- Información del curso encontrado (nombre y nota)
- Si no existe: "Curso no encontrado"
- Si el nombre está vacío: "Nombre inválido"
- Si no hay cursos: "No hay cursos registrados"

**Diferencia con la opción 5:**
La búsqueda binaria es más rápida cuando hay muchos cursos registrados, pero requiere que la lista esté ordenada (el programa hace esto automáticamente).

---

### 5.11 Simular Cola de Solicitudes de Revisión (Opción 11)

**Descripción:**
Gestiona una cola de solicitudes para revisar notas de cursos. Funciona bajo el principio FIFO (First In, First Out - Primero en entrar, primero en salir).

**Submenú disponible:**
```
--- Cola de Solicitudes de Revisión ---
1. Agregar solicitud de revisión
2. Atender siguiente solicitud
3. Ver cola de solicitudes
4. Volver al menú principal
```

#### 5.11.1 Agregar Solicitud de Revisión

**Datos de entrada:**
- Nombre del curso a revisar (texto)

**Validaciones:**
- Debe haber cursos registrados
- El curso debe existir en el sistema
- El nombre no puede estar vacío

**Ejemplo:**
```
Seleccione una opción: 1
Nombre del curso a revisar: Matemáticas
Solicitud de revisión agregada para: Matemáticas
```

#### 5.11.2 Atender Siguiente Solicitud

**Descripción:**
Atiende y elimina la solicitud más antigua de la cola (la primera que se agregó).

**Datos de entrada:**
Ninguno

**Ejemplo:**
```
Seleccione una opción: 2
Atendiendo solicitud de: Matemáticas
```

**Salida esperada:**
- Nombre del curso atendido
- Si no hay solicitudes: "No hay solicitudes pendientes"

#### 5.11.3 Ver Cola de Solicitudes

**Descripción:**
Muestra todas las solicitudes pendientes en orden.

**Datos de entrada:**
Ninguno

**Ejemplo:**
```
Seleccione una opción: 3
Solicitudes pendientes:
1. Matemáticas
2. Historia
3. Física
```

**Salida esperada:**
- Lista numerada de solicitudes pendientes
- Si no hay solicitudes: "No hay solicitudes pendientes"

---

### 5.12 Mostrar Historial de Cambios (Opción 12)

**Descripción:**
Muestra un registro de todos los cambios realizados en el sistema (registros, actualizaciones y eliminaciones) en orden LIFO (Last In, First Out - Último en entrar, primero en salir).

**Datos de entrada:**
Ninguno

**Cambios registrados:**
- Registro de nuevos cursos
- Actualizaciones de notas
- Eliminación de cursos

**Ejemplo de uso:**
```
Seleccione una opción: 12
Historial de cambios (más reciente primero):
1. Actualizada nota de Historia: 65.0 -> 70.0
2. Eliminado curso: Química
3. Registrado curso: Física con nota 92.5
4. Registrado curso: Historia con nota 65.0
5. Registrado curso: Matemáticas con nota 85.0
```

**Salida esperada:**
- Lista numerada de cambios (del más reciente al más antiguo)
- Si no hay cambios: "No hay cambios registrados en el historial"

**Nota:** El historial se mantiene durante toda la sesión del programa. Al cerrar el programa, el historial se pierde.

---

### 5.13 Salir (Opción 13)

**Descripción:**
Cierra el programa de manera ordenada.

**Datos de entrada:**
Ninguno

**Ejemplo de uso:**
```
Seleccione una opción: 13
Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!
```

**Advertencia:** Al salir del programa, todos los datos se perderán. El sistema no guarda información de forma permanente.

---

## 6. Ejemplos de Uso

### Ejemplo 1: Flujo Básico de Uso

**Objetivo:** Registrar tres cursos, ver el promedio y ordenarlos por nota.

```
Paso 1: Ejecutar el programa
python menu.py

Paso 2: Registrar primer curso
Seleccione una opción: 1
Nombre del curso: Matemáticas
Nota del curso (0 a 100): 85
Curso registrado

Paso 3: Registrar segundo curso
Seleccione una opción: 1
Nombre del curso: Historia
Nota del curso (0 a 100): 70
Curso registrado

Paso 4: Registrar tercer curso
Seleccione una opción: 1
Nombre del curso: Física
Nota del curso (0 a 100): 92
Curso registrado

Paso 5: Ver todos los cursos
Seleccione una opción: 2
Listado de cursos:
1. Matemáticas - Nota: 85.0
2. Historia - Nota: 70.0
3. Física - Nota: 92.0

Paso 6: Calcular promedio
Seleccione una opción: 3
Promedio general: 82.33

Paso 7: Ordenar por nota
Seleccione una opción: 8
Cursos ordenados por nota (menor a mayor)
1. Historia - Nota: 70.0
2. Matemáticas - Nota: 85.0
3. Física - Nota: 92.0
```

### Ejemplo 2: Actualizar y Ver Historial

**Objetivo:** Actualizar una nota y verificar el historial de cambios.

```
Paso 1: Actualizar nota
Seleccione una opción: 6
Nombre del curso a actualizar: Historia
Nueva nota (0 a 100): 75
Nota actualizada

Paso 2: Ver historial
Seleccione una opción: 12
Historial de cambios (más reciente primero):
1. Actualizada nota de Historia: 70.0 -> 75.0
2. Registrado curso: Física con nota 92.0
3. Registrado curso: Historia con nota 70.0
4. Registrado curso: Matemáticas con nota 85.0
```

### Ejemplo 3: Gestionar Cola de Revisiones

**Objetivo:** Agregar solicitudes de revisión y atenderlas.

```
Paso 1: Entrar al menú de cola
Seleccione una opción: 11

Paso 2: Agregar primera solicitud
--- Cola de Solicitudes de Revisión ---
Seleccione una opción: 1
Nombre del curso a revisar: Matemáticas
Solicitud de revisión agregada para: Matemáticas

Paso 3: Agregar segunda solicitud
Seleccione una opción: 1
Nombre del curso a revisar: Historia
Solicitud de revisión agregada para: Historia

Paso 4: Ver cola
Seleccione una opción: 3
Solicitudes pendientes:
1. Matemáticas
2. Historia

Paso 5: Atender primera solicitud
Seleccione una opción: 2
Atendiendo solicitud de: Matemáticas

Paso 6: Ver cola actualizada
Seleccione una opción: 3
Solicitudes pendientes:
1. Historia

Paso 7: Volver al menú principal
Seleccione una opción: 4
```

### Ejemplo 4: Búsqueda de Cursos

**Objetivo:** Comparar búsqueda lineal y binaria.

```
Paso 1: Búsqueda lineal
Seleccione una opción: 5
Nombre del curso a buscar: física
Curso: Física - Nota: 92.0

Paso 2: Búsqueda binaria
Seleccione una opción: 10
Nombre del curso a buscar: FÍSICA
Curso: Física - Nota: 92.0
```

**Nota:** Ambas búsquedas encuentran el curso sin importar mayúsculas o minúsculas.

