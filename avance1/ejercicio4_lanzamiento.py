# Archivo: ejercicio4_lanzamiento.py
# Curso: Principios de Programación 1 - SOFT-01
# Sección: SCV6
# Integrante: Katherine Angulo Angulo
# Fecha: octubre de 2026
# Versión: 1.0
# Propósito: Verificar si se cumplen las condiciones para autorizar el lanzamiento.
# Constante de la misión
RESERVA_COMBUSTIBLE = 10
# Entrada de datos
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))
# Cálculo del combustible total
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)
# Verificación de las condiciones para el lanzamiento

if (
    combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
