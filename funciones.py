def cargar_producto(inventario: list[list], nombre: str, precio: float, cantidad: int) -> list[list]:
    '''
    Carga un producto al inventario.\n
    Parámetros: inventario (list[list]), nombre (str), precio (float), cantidad (int).\n
    Retorno: inventario (list[list])
    '''
    elemento = [nombre, precio, cantidad]
    inventario.append(elemento)

    return inventario

def validar_precio_o_cantidad(dato: float | int) -> bool:
    '''
    Verifica que el precio o la cantidad sean mayores a cero.\n
    Parámetros: dato (float | int).\n
    Retorno: dato_valido (bool).
    '''
    if (dato > 0):
        dato_valido = True
    else:
        dato_valido = False
    
    return dato_valido


def ingresar_nombre() -> str:
    '''
    Permite ingresar el nombre del producto.\n
    Retorno: nombre (str).
    '''
    nombre = input("Ingrese el nombre del producto: ")

    return nombre

def ingresar_precio() -> float:
    '''
    Permite ingresar el precio del producto.\n
    Retorno: precio (float).
    '''
    precio = float(input("Ingrese el precio del producto (debe ser mayor a 0): "))
    precio_valido = validar_precio_o_cantidad(precio)

    while (precio_valido == False):
        precio = float(input("Error. Ingrese un valor mayor a 0: "))
        precio_valido = validar_precio_o_cantidad(precio)
    
    return precio

def ingresar_cantidad() -> int:
    '''
    Permite ingresar la cantidad del producto.\n
    Retorno: cantidad (int).
    '''
    cantidad = int(input("Ingrese la cantidad del producto (debe ser mayor a 0): "))
    cantidad_valida = validar_precio_o_cantidad(cantidad)

    while (cantidad_valida == False):
        cantidad = int(input("Error. Ingrese un valor mayor a 0: "))
        cantidad_valida = validar_precio_o_cantidad(cantidad)
    
    return cantidad

def buscar_producto(inventario: list[list], nombre: str) -> str:
    '''
    Busca el nombre de un producto en el inventario.\n
    Parámetros: inventario (list[list]), nombre (str).
    Retorno: mensaje (str).
    '''
    mensaje = "No se encontró un producto con ese nombre."

    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if (inventario[i][0] == nombre):
                mensaje = f"¡Producto Encontrado!\nDatos del Producto:\nNombre: {inventario[i][0]}.\nPrecio: {inventario[i][1]}\nCantidad: {inventario[i][2]}"
                break
    
    return mensaje

def ordenar_inventario(inventario: list[list]) -> list[list]:
    '''
    Ordena el inventario de menor precio a mayor precio.\n
    Parámetro: inventario (list[list]).
    Retorno: inventario (list[list]).
    '''
    for i in range(len(inventario)):
        for j in range(0, len(inventario) - i - 1):
            if (inventario[j][1] > inventario[j+1][1]):
                temp = inventario[j]
                inventario[j] = inventario[j+1]
                inventario[j+1] = temp
    
    return inventario

def encontrar_mas_caro(inventario: list[list]) -> list:
    '''
    Busca el producto más caro del inventario.\n
    Parámetro: inventario (list[list]).\n
    Retorno: elemento_mas_caro (list).
    '''
    flag_primero = True

    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            precio = inventario[i][1]
            if (flag_primero):
                nombre_mas_caro = inventario[i][0]
                precio_mas_caro = inventario[i][1]
                cantidad_mas_caro = inventario[i][2]
                flag_primero = False
            else:
                if (precio > precio_mas_caro):
                    nombre_mas_caro = inventario[i][0]
                    precio_mas_caro = inventario[i][1]
                    cantidad_mas_caro = inventario[i][2]
    
    elemento_mas_caro = [nombre_mas_caro, precio_mas_caro, cantidad_mas_caro]
    return elemento_mas_caro

def encontrar_mas_barato(inventario: list[list]) -> list:
    '''
    Busca el producto más barato del inventario.\n
    Parámetro: inventario (list[list]).\n
    Retorno: elemento_mas_barato (list).
    '''
    flag_primero = True

    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            precio = inventario[i][1]
            if (flag_primero):
                nombre_mas_barato = inventario[i][0]
                precio_mas_barato = inventario[i][1]
                cantidad_mas_barato = inventario[i][2]
                flag_primero = False
            else:
                if (precio < precio_mas_barato):
                    nombre_mas_barato = inventario[i][0]
                    precio_mas_barato = inventario[i][1]
                    cantidad_mas_barato = inventario[i][2]
        
    elemento_mas_barato = [nombre_mas_barato, precio_mas_barato, cantidad_mas_barato]
    return elemento_mas_barato

def encontrar_precios_mayores(inventario: list[list]) -> list[list] | str:
    '''
    Busca si el inventario tiene productos con precio mayor a 15000.\n
    Parámetro: inventario (list[list]).\n
    Retorno: mensaje (list[list] | str).
    '''
    precio_comparado = 15000
    lista_mayores = []
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            precio_producto = inventario[i][1]
            if (precio_producto > precio_comparado):
                lista_mayores.append(inventario[i])
    
    if (len(lista_mayores) == 0):
        retorno = "No se encontraron productos con precio mayor a 15000."
    else:
        retorno = lista_mayores
    
    return retorno