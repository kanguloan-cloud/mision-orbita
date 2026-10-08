# Archivo: ejercicio2_combustible.py
# Curso: Principios de Programación 1 - SOFT-01
# Sección: SCV6
# Integrante: Katherine Angulo Angulo
# Fecha: octubre de 2026
# Versión: 1.0
# Propósito: Verificar si el combustible disponible es suficiente para la misión.
# Constante de la misión
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

# Cálculos
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

combustible_adicional = combustible_disponible - combustible_total

# Verificación del margen de combustible
if combustible_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")

# Mostrar resultados
print("\n--- RESULTADOS DE COMBUSTIBLE ---")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")
