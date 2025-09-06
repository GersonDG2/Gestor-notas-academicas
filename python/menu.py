# python/menu.py
from registrar_curso import ejecutar as opcion_1
from mostrar_cursos import ejecutar as opcion_2
from promedio_general import ejecutar as opcion_3
from contar_aprobados import ejecutar as opcion_4
from buscar_curso import ejecutar as opcion_5
from actualizar_nota import ejecutar as opcion_6

def mostrar_menu():
    print("====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (burbuja)")
    print("9. Ordenar cursos por nombre (inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")

def main():
    while True:
        mostrar_menu()
        op = input("Seleccione una opción: ").strip()
        try:
            opcion = int(op)
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            continue

        if opcion == 1:
            opcion_1()
        elif opcion == 2:
            opcion_2()
        elif opcion == 3:
            opcion_3()
        elif opcion == 4:
            opcion_4()
        elif opcion == 5:
            opcion_5()
        elif opcion == 6:
            opcion_6()
        elif opcion == 7:
            print("Opción en construcción")
        elif opcion == 8:
            print("Opción en construcción")
        elif opcion == 9:
            print("Opción en construcción")
        elif opcion == 10:
            print("Opción en construcción")
        elif opcion == 11:
            print("Opción en construcción")
        elif opcion == 12:
            print("Opción en construcción")
        elif opcion == 13:
            print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        print()

if __name__ == "__main__":
    main()