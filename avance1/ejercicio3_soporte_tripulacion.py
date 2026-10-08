# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: Principios de Programación 1 - SOFT-01
# Sección: SCV6
# Integrante: Katherine Angulo Angulo
# Fecha: octubre de 2026
# Versión: 1.0
# Propósito: Verificar si hay suficiente oxígeno y provisiones para la tripulación.
# Entrada de datos
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))
# Verificación de los recursos

if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
