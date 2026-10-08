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