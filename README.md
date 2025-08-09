# Gestor de notas académicas

## Descripción
Este proyecto es un programa en consola que permite a un estudiante registrar y gestionar las calificaciones de sus cursos. Está dirigido a personas que quieran organizar sus notas, calcular promedios y realizar búsquedas o análisis simples.
Su objetivo es ofrecer una herramienta básica para almacenar, consultar y analizar el rendimiento académico, cubriendo la necesidad de un control sencillo y rápido de notas.

## Requisitos del sistema
### Requisitos funcionales
El menú del sistema incluye, entre otras, las siguientes funcionalidades:

- **Registrar nuevo curso:** Permite añadir un nuevo curso con su respectiva nota.
- **Mostrar todos los cursos y notas:** Visualiza la lista completa de cursos registrados.
- **Calcular promedio general:** Calcula y muestra el promedio de todas las notas.
- **Contar cursos aprobados y reprobados:** Muestra un recuento de los cursos según su estado (aprobado/reprobado).
- **Buscar curso por nombre (búsqueda lineal):** Busca un curso específico en la lista.
- **Actualizar nota de un curso:** Modifica la calificación de un curso ya existente.
- **Eliminar un curso:** Borra un curso de la lista.
- **Ordenar cursos por nota (burbuja):** Ordena la lista de cursos de menor a mayor nota.
- **Ordenar cursos por nombre (inserción):** Ordena la lista alfabéticamente por el nombre del curso.
- **Buscar curso por nombre (búsqueda binaria):** Realiza una búsqueda optimizada por nombre (requiere lista ordenada).
- **Simular cola de solicitudes de revisión:** Gestiona una cola de peticiones para revisar notas.
- **Mostrar historial de cambios (pila):** Muestra los últimos cambios realizados en las notas.

### Requisitos no funcionales
- El sistema se ejecuta únicamente en consola con Python.
- No utiliza librerías externas.
- Debe estar desarrollado con funciones, listas, bucles y condicionales.
- Las estructuras de control deben implementarse también en pseudocódigo.
- La interfaz se basa en un menú interactivo que se repite hasta que el usuario decida salir.
