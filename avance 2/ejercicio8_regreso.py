
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01, sección C3-2026
# Integrante: Katherine Angulo Angulo
# Fecha: 08/11/2026
# Versión: 1.0
# Descripción: Evalúa el regreso de la nave y la supervivencia
# de la tripulación según los recursos disponibles.

# Declaración de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_ida = int(input("Ingrese los días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Cálculo del combustible necesario para regresar
combustible_regreso = dias_ida * CONSUMO_COMBUSTIBLE_DIA

# Caso A: existe combustible suficiente para iniciar el regreso
if combustible >= combustible_regreso:
    dias_completados = 0
    dia_actual = 1
    regreso_completo = True

    # Simulación del consumo de recursos durante cada día
    while dia_actual <= dias_ida and regreso_completo:
        consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
        consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

        if (oxigeno >= consumo_oxigeno
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= consumo_provisiones):

            combustible -= CONSUMO_COMBUSTIBLE_DIA
            oxigeno -= consumo_oxigeno
            energia -= CONSUMO_ENERGIA_DIA
            provisiones -= consumo_provisiones

            dias_completados += 1

            print(
                f"Día {dia_actual} | Combustible: {combustible} | "
                f"Oxígeno: {oxigeno} | Energía: {energia} | "
                f"Provisiones: {provisiones}"
            )

            dia_actual += 1

        else:
            regreso_completo = False

    # Salida de resultados del caso A
    if regreso_completo:
        print("La tripulación regresó exitosamente a la Tierra.")
        print(f"Combustible restante: {combustible} unidades")
        print(f"Oxígeno restante: {oxigeno} unidades")
        print(f"Energía restante: {energia} unidades")
        print(f"Provisiones restantes: {provisiones} unidades")

    else:
        print(f"El regreso se interrumpió en el día {dias_completados + 1}.")

        # Identificación de todos los recursos insuficientes
        if oxigeno < consumo_oxigeno:
            print("Recurso insuficiente: oxígeno")

        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")

        if provisiones < consumo_provisiones:
            print("Recurso insuficiente: provisiones")

        print("La tripulación no completó el regreso.")

# Caso B: no existe combustible suficiente para regresar
else:
    print("La tripulación quedó varada en el destino.")

    # Cálculo de los días de supervivencia por recurso
    dias_oxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE)
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // tripulantes

    print(f"Días por oxígeno: {dias_oxigeno}")
    print(f"Días por energía: {dias_energia}")
    print(f"Días por provisiones: {dias_provisiones}")

    # Determinación del menor valor mediante condicionales
    supervivencia = dias_oxigeno

    if dias_energia < supervivencia:
        supervivencia = dias_energia

    if dias_provisiones < supervivencia:
        supervivencia = dias_provisiones

    print(f"Supervivencia estimada: {supervivencia} días")

    # Identificación de todos los recursos limitantes
    recursos_limitantes = ""

    if dias_oxigeno == supervivencia:
        recursos_limitantes = "oxígeno"

    if dias_energia == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes += ", energía"

    if dias_provisiones == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes += ", provisiones"

    print(f"Recurso(s) limitante(s): {recursos_limitantes}")
