# Archivo: mision_orbita.py
# Curso: Principios de Programación 1 - SOFT-01
# Sección: SCV6
# Integrante: Katherine Angulo Angulo
# Fecha: octubre de 2026
# Versión: 1.0
# Propósito: Calcular los recursos necesarios para una misión espacial.
# Constantes de la misión
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10

CONSUMO_OXIGENO_DIA = 2
FACTOR_IDA_REGRESO = 2
RESERVA_OXIGENO = 5

CONSUMO_ENERGIA_DIA = 5
RESERVA_ENERGIA = 10

CONSUMO_PROVISION_DIA = 1
RESERVA_PROVISIONES = 3
# Entrada de datos
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados de viaje: "))
# Cálculos de combustible
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA

combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)
# Cálculo de oxígeno
oxigeno_requerido = (
    dias_viaje
    * CONSUMO_OXIGENO_DIA
    * FACTOR_IDA_REGRESO
    * tripulantes
    + RESERVA_OXIGENO
)
# Cálculo de energía
energia_requerida = (
    dias_viaje
    * CONSUMO_ENERGIA_DIA
    * FACTOR_IDA_REGRESO
    + RESERVA_ENERGIA
)

# Cálculo de provisiones
provisiones_requeridas = (
    dias_viaje
    * tripulantes
    * CONSUMO_PROVISION_DIA
    * FACTOR_IDA_REGRESO
    + RESERVA_PROVISIONES
)
# Mostrar resultados
print("\n--- RESULTADOS DE LA MISIÓN ---")
print("Misión:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duración estimada:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
