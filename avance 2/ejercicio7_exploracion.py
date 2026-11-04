# Proyecto: Misión Órbita - Avance 2
# Ejercicio 7: Actividades de exploración científica
# Estudiante: Katherine Angulo Angulo
# Descripción: Simula las actividades científicas de una tripulación.

# Constantes de las opciones del menú
OPCION_ANALIZAR = 1
OPCION_RECOLECTAR = 2
OPCION_OBSERVAR = 3
OPCION_FINALIZAR = 4

# Costos y puntos de la actividad 1: Analizar terreno
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

# Costos y puntos de la actividad 2: Recolectar muestra
ENERGIA_RECOLECTAR = 12
PROVISIONES_RECOLECTAR = 2
PUNTOS_RECOLECTAR = 20

# Costos y puntos de la actividad 3: Realizar observación
ENERGIA_OBSERVAR = 5
PROVISIONES_OBSERVAR = 0
PUNTOS_OBSERVAR = 8

# Entrada de recursos disponibles
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_activa = True

# Ciclo principal de la exploración
while exploracion_activa:
    print("\n--- Actividades de exploración científica ---")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una actividad: "))

    if opcion == OPCION_ANALIZAR:
        nombre_actividad = "Analizar terreno"
        energia_actividad = ENERGIA_ANALIZAR
        provisiones_actividad = PROVISIONES_ANALIZAR
        puntos_actividad = PUNTOS_ANALIZAR

    elif opcion == OPCION_RECOLECTAR:
        nombre_actividad = "Recolectar muestra"
        energia_actividad = ENERGIA_RECOLECTAR
        provisiones_actividad = PROVISIONES_RECOLECTAR
        puntos_actividad = PUNTOS_RECOLECTAR

    elif opcion == OPCION_OBSERVAR:
        nombre_actividad = "Realizar observación"
        energia_actividad = ENERGIA_OBSERVAR
        provisiones_actividad = PROVISIONES_OBSERVAR
        puntos_actividad = PUNTOS_OBSERVAR

    elif opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        exploracion_activa = False

    else:
        print("Opción no válida.")

    # Verificación y ejecución de las actividades
    if (
        exploracion_activa
        and opcion >= OPCION_ANALIZAR
        and opcion <= OPCION_OBSERVAR
    ):
        if (
            energia >= energia_actividad
            and provisiones >= provisiones_actividad
        ):
            energia -= energia_actividad
            provisiones -= provisiones_actividad
            actividades_realizadas += 1
            puntos_cientificos += puntos_actividad

            if opcion == OPCION_RECOLECTAR:
                muestras_recolectadas += 1

            print(
                f"Actividad realizada: {nombre_actividad}. "
                f"Puntos obtenidos: {puntos_actividad}"
            )

        else:
            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )
            exploracion_activa = False

# Resumen final de la exploración
print("\n--- Resumen de la exploración ---")
print(f"Actividades realizadas: {actividades_realizadas}")
print(f"Muestras recolectadas: {muestras_recolectadas}")
print(f"Puntos científicos: {puntos_cientificos}")
print(f"Energía restante: {energia} unidades")
print(f"Provisiones restantes: {provisiones} unidades")
