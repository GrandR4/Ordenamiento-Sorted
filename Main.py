# Ordenamiento-Sorted

repuestos = [
    {"nombre": "Filtro de aceite", "precio": 15.99},
    {"nombre": "Bujía", "precio": 5.49},
    {"nombre": "Pastillas de freno", "precio": 35.99},
    {"nombre": "Batería", "precio": 120.00},
    {"nombre": "Aceite de motor", "precio": 45.50},
    {"nombre": "Filtro de aire", "precio": 20.00},
]


def mostrar_repuestos(lista):
    print("=" * 50)
    print("Repuestos disponibles:")
    for repuesto in lista:
        print(f"{repuesto['nombre']} - ${repuesto['precio']:.2f}")
    print("=" * 50)
    

def ordenar_repuestos_por_precio(lista, clave, ascendente=True):
    lista.sort(key=lambda x: x[clave], reverse=not ascendente)


def menu():
    while True:
        print("\nTienda  CarFix")
        print("1. Mostrar repuestos")
        print("2. Ordenar repuestos por precio (Menor a Mayor)")
        print("3. Ordenar repuestos por precio (Mayor a menor)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_repuestos(repuestos)
        elif opcion == "2":
            ordenar_repuestos_por_precio(repuestos, clave="precio", ascendente=True)
            mostrar_repuestos(repuestos)
        elif opcion == "3":
            ordenar_repuestos_por_precio(repuestos, clave="precio", ascendente=False)
            mostrar_repuestos(repuestos)
        elif opcion == "4":
            print("Gracias por visitar nuestra CarFix. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")




menu()
