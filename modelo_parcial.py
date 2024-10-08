from funciones import *

inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30]
]

salir = False

while (salir == False):

    print("")
    print("Bienvenido a Empire Inventory. Elija una de las siguientes opciones:")
    print("1. Cargar 1 producto.")
    print("2. Buscar producto.")
    print("3. Ordenar inventario.")
    print("4. Mostrar producto más caro y más barato.")
    print("5. Mostrar productos con precio mayor a 15000 (NO FUNCIONA CORRECTAMENTE).")
    print("6. Salir.")
    print("")

    opcion = input("Ingrese una de las opciones: ")
    print("")

    while (opcion != "1") and (opcion != "2") and (opcion != "3") and (opcion != "4") and (opcion != "5") and (opcion != "6"):
        opcion = input("Opción Inválida. Ingrésela nuevamente: ")

    match opcion:
        case "1":
            print(f"Opción Seleccionada: {opcion}. Cargar 1 producto.")
            nombre = ingresar_nombre()
            nombre = nombre.capitalize()
            nombre_ya_usado = buscar_nombre(nombre, inventario)

            while (nombre_ya_usado == True):
                print("Error. Nombre ya en uso.")
                nombre = ingresar_nombre()
                nombre = nombre.capitalize()
                nombre_ya_usado = buscar_nombre(nombre, inventario)

            precio = ingresar_precio()
            cantidad = ingresar_cantidad()
            inventario = cargar_producto(inventario, nombre, precio, cantidad)
        case "2":
            print(f"Opción Seleccionada: {opcion}. Buscar producto.")
            nombre_a_buscar = ingresar_nombre()
            nombre_a_buscar = nombre_a_buscar.capitalize()
            print("")
            resultado_busqueda = buscar_producto(inventario, nombre_a_buscar)
            print(resultado_busqueda)
        case "3":
            inventario_ordenado = ordenar_inventario(inventario)
            for i in range(len(inventario_ordenado)):
                print(inventario_ordenado[i])
        case "4":
            print(f"Opción Seleccionada: {opcion}. Mostrar producto más caro y más barato.")
            elemento_mas_caro = encontrar_mas_caro(inventario)
            elemento_mas_barato = encontrar_mas_barato(inventario)
            print(f"Producto Más Caro: {elemento_mas_caro}\nProducto Más Barato: {elemento_mas_barato}")
        case "5":
            print(f"Opción Seleccionada: {opcion}. Mostrar productos con precio mayor a 15000.")
            resultado_mayores = encontrar_precios_mayores(inventario)
            print(resultado_mayores)
        case "6":
            print("¡Gracias por su visita!")
            salir = True