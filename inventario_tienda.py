
# Programa: Inventario de una tienda
# Curso: Principios de Programación 1
# Propósito: Registrar productos y calcular el valor del inventario.

LIMITE_REPOSICION = 5

valor_total = 0
productos_registrados = 0
productos_reposicion = 0

respuesta = input("¿Desea registrar un producto? (s/n): ").lower()

while respuesta == "s":
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_unitario = float(input("Ingrese el precio unitario: ₡"))
    cantidad_existencia = int(input("Ingrese la cantidad en existencia: "))

    if precio_unitario <= 0:
        print("Error: el precio debe ser mayor que cero.")
        print("El producto no se registrará.")

    else:
        valor_producto = precio_unitario * cantidad_existencia
        valor_total = valor_total + valor_producto
        productos_registrados = productos_registrados + 1

        if cantidad_existencia < LIMITE_REPOSICION:
            print("El producto requiere reposición.")
            productos_reposicion = productos_reposicion + 1
        else:
            print("El producto no requiere reposición.")

        print("Producto registrado:", nombre_producto)
        print("Valor del producto: ₡", valor_producto)

    respuesta = input(
        "¿Desea registrar otro producto? (s/n): "
    ).lower()

print("\n--- RESULTADOS FINALES DEL INVENTARIO ---")
print("Valor total del inventario: ₡", valor_total)
print("Cantidad de productos registrados:", productos_registrados)
print("Cantidad de productos que requieren reposición:", productos_reposicion)

