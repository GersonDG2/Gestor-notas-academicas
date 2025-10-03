# Gestor de notas académicas

## Descripción
Este proyecto es un programa en consola que permite a un estudiante registrar y gestionar las calificaciones de sus cursos. Está dirigido a personas que quieran organizar sus notas, calcular promedios y realizar búsquedas o análisis simples.
Su objetivo es ofrecer una herramienta básica para almacenar, consultar y analizar el rendimiento académico, cubriendo la necesidad de un control sencillo y rápido de notas.

## Requisitos del sistema
### Requisitos funcionales
El menú del sistema incluye las siguientes funcionalidades:

#### Funcionalidades implementadas
- **Registrar nuevo curso:** Permite añadir un nuevo curso con su respectiva nota (0-100). Registra el cambio en el historial.
- **Mostrar todos los cursos y notas:** Visualiza la lista completa de cursos registrados con sus notas.
- **Calcular promedio general:** Calcula y muestra el promedio de todas las notas registradas.
- **Contar cursos aprobados y reprobados:** Muestra un recuento de los cursos según su estado (aprobado ≥60, reprobado <60).
- **Buscar curso por nombre (búsqueda lineal):** Busca un curso específico en la lista mediante búsqueda secuencial.
- **Actualizar nota de un curso:** Modifica la calificación de un curso ya existente (0-20). Registra el cambio en el historial.
- **Eliminar un curso:** Borra un curso de la lista. Registra el cambio en el historial.
- **Ordenar cursos por nota (burbuja):** Ordena la lista de cursos de menor a mayor nota usando el algoritmo de ordenamiento burbuja.
- **Ordenar cursos por nombre (inserción):** Ordena la lista alfabéticamente por el nombre del curso usando el algoritmo de ordenamiento por inserción.
- **Simular cola de solicitudes de revisión:** Gestiona una cola (FIFO) de peticiones para revisar notas. Permite agregar solicitudes, atender la siguiente y ver la cola completa.
- **Mostrar historial de cambios (pila):** Muestra los últimos cambios realizados (registros, actualizaciones y eliminaciones) en orden LIFO (del más reciente al más antiguo).

#### Funcionalidades pendientes
- **Buscar curso por nombre (búsqueda binaria):** Realiza una búsqueda optimizada por nombre (requiere lista ordenada).

### Requisitos no funcionales
- El sistema se ejecuta únicamente en consola con Python.
- No utiliza librerías externas.
- Debe estar desarrollado con funciones, listas, bucles y condicionales.
- Las estructuras de control deben implementarse también en pseudocódigo.
- La interfaz se basa en un menú interactivo que se repite hasta que el usuario decida salir.

## Cambios recientes

### Los cambios hechos esta semana son los siguientes:

#### 1. Ordenar cursos por nota con burbuja
Agregué la opción para ordenar los cursos de menor a mayor nota. Usé el algoritmo burbuja que vimos en clase.

**Lo que me costó:**
- Al principio no entendía bien cómo funcionaban los dos for anidados del algoritmo burbuja.
- Me confundí varias veces al comparar las notas porque están dentro de diccionarios, no son números sueltos.
- Tuve que practicar varias veces el intercambio de elementos con la variable temporal.

**Lo que aprendí:**
- Ahora entiendo cómo funciona el algoritmo burbuja, básicamente va comparando pares de elementos y los intercambia si están en el orden incorrecto.
- Aprendí a trabajar con listas que tienen diccionarios adentro y cómo acceder a sus valores.
- Me quedó claro por qué se usa una variable temporal para intercambiar elementos.
- Vi la importancia de manejar bien los índices para que no se salga del rango de la lista.

#### 2. Ordenar cursos por nombre con inserción
Esta fue la opción para ordenar alfabéticamente los cursos. Usé el algoritmo de inserción que es diferente al burbuja.

**Lo que me costó:**
- Me costó entender la diferencia entre burbuja e inserción, son parecidos pero funcionan distinto.
- El while dentro del for me confundió al principio.
- Tuve que investigar cómo hacer que no importe si escribo mayúsculas o minúsculas al ordenar.
- Me preocupaba que se perdieran datos al mover los elementos.

**Lo que aprendí:**
- El algoritmo de inserción funciona como cuando ordenas cartas en tu mano, vas insertando cada elemento en su lugar correcto.
- Descubrí el método .lower() que sirve para comparar textos sin importar mayúsculas.
- Practiqué usar while dentro de for, que al principio me parecía raro pero tiene sentido.
- Entendí que en Python cuando mueves objetos completos (los diccionarios) no se pierden los datos.

#### 3. Historial de cambios usando pilas
Hice un sistema que guarda automáticamente todo lo que hago en el programa (cuando registro, actualizo o elimino cursos). Usé una pila para esto.

**Lo que me costó:**
- El concepto de pila (LIFO) era nuevo para mí, tuve que leer varias veces qué significa.
- Me daba miedo romper el código que ya funcionaba al agregar el historial.
- No sabía bien qué información guardar de cada cambio.
- Mostrar la lista al revés me tomó un rato entenderlo.

**Lo que aprendí:**
- Una pila es como una pila de platos, el último que pones es el primero que sacas (LIFO).
- Aprendí a importar funciones de un archivo a otro para reutilizar código.
- Los f-strings son súper útiles para crear mensajes con variables adentro.
- Para recorrer una lista al revés se puede usar range con números negativos.
- Es importante guardar los datos antes de borrarlos, si no se pierden para siempre.

#### 4. Cola de solicitudes de revisión
Creé un sistema para manejar solicitudes de revisión de notas usando una cola. Tiene su propio menú con varias opciones.

**Lo que me costó:**
- Entender qué es una cola (FIFO) y en qué se diferencia de la pila.
- Hacer un menú dentro de otro menú fue complicado.
- Validar que el curso exista antes de agregarlo a la cola.
- Usar pop(0) en vez de solo pop() me confundió al inicio.

**Lo que aprendí:**
- Una cola es como la fila del banco, el primero que llega es el primero que atienden (FIFO).
- La diferencia entre pila y cola está en el orden: pila es último en entrar primero en salir, cola es primero en entrar primero en salir.
- append() sirve para agregar al final y pop(0) para sacar del inicio, así funciona una cola.
- Los menús anidados se hacen con otro while, solo hay que tener cuidado con los breaks.
- Siempre hay que validar los datos antes de usarlos, si no el programa puede fallar.
- Es bueno mostrar mensajes claros cuando no hay datos para que el usuario sepa qué pasa.
