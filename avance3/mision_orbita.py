# ============================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Katherine Angulo Angulo
# Fecha: 20/11/2026
# Versión: 1.1
# Descripción: Sistema integrado Misión Órbita para planificar,
# ejecutar y registrar misiones de exploración espacial.
# ============================================================

# ============================================================
# CONSTANTES DE LA MISIÓN
# ============================================================

# Destinos: (nombre, días de viaje de ida)
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))

# Actividades: (nombre, combustible, energía, provisiones, puntos)
ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# Columnas de DESTINOS: (nombre, días)
DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES: (nombre, combustible, energía, provisiones, puntos)
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posición de cada recurso en las listas recursos, requeridos y consumo
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la matriz bitácora: [numero, actividad, puntos]
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas de la matriz historial: [numero, nombre, destino, resultado, puntos]
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes numéricas de las fórmulas
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1
CANTIDAD_TRAYECTOS = 2
RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
RESERVA_ENERGIA = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10


# ============================================================
# COMPONENTE A: PREPARACIÓN Y AUTORIZACIÓN
# ============================================================

def mostrar_destinos():
    print("Destinos disponibles:")
    for indice in range(len(DESTINOS)):
        nombre = DESTINOS[indice][DES_NOMBRE]
        dias = DESTINOS[indice][DES_DIAS]
        print(str(indice + 1) + ". " + nombre + " (" + str(dias) + " días)")


def leer_recursos():
    recursos = []
    for recurso in RECURSOS:
        cantidad = int(input("Cantidad disponible de " + recurso + ": "))
        recursos.append(cantidad)
    return recursos


def calcular_requeridos(dias_viaje, tripulantes):
    requeridos = []
    combustible = (dias_viaje * CONSUMO_COMBUSTIBLE_DIA
                   * CANTIDAD_TRAYECTOS + RESERVA_COMBUSTIBLE)
    oxigeno = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE
               * CANTIDAD_TRAYECTOS * tripulantes + OXIGENO_EMERGENCIA)
    energia = (dias_viaje * CONSUMO_ENERGIA_DIA
               * CANTIDAD_TRAYECTOS + RESERVA_ENERGIA)
    provisiones = (dias_viaje * tripulantes
                   * CANTIDAD_TRAYECTOS + PROVISIONES_ADICIONALES)
    requeridos.append(combustible)
    requeridos.append(oxigeno)
    requeridos.append(energia)
    requeridos.append(provisiones)
    return requeridos


def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje,
                    tripulantes, disponibles, requeridos):
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)
    for indice in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[indice].capitalize()
        cantidad_disponible = disponibles[indice]
        cantidad_requerida = requeridos[indice]
        print(nombre_recurso + ": disponible", cantidad_disponible,
              "| requerido", cantidad_requerida)
    margen_combustible = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print("Margen adicional de combustible:", margen_combustible, "unidades")
    if margen_combustible < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


def autorizar_lanzamiento(disponibles, requeridos):
    autorizado = True
    for indice in range(len(RECURSOS)):
        if disponibles[indice] < requeridos[indice]:
            autorizado = False
    return autorizado


# ============================================================
# COMPONENTE B: VIAJE DE IDA
# ============================================================

def calcular_consumo_diario(tripulantes):
    consumo = []
    combustible = CONSUMO_COMBUSTIBLE_DIA
    oxigeno = CONSUMO_OXIGENO_TRIPULANTE * tripulantes
    energia = CONSUMO_ENERGIA_DIA
    provisiones = CONSUMO_PROVISIONES_TRIPULANTE * tripulantes
    consumo.append(combustible)
    consumo.append(oxigeno)
    consumo.append(energia)
    consumo.append(provisiones)
    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    for indice in range(len(RECURSOS)):
        recursos[indice] = recursos[indice] - consumo[indice] * dias_viaje
    return recursos


def recursos_alcanzan(recursos, consumo):
    alcanza = True
    for indice in range(len(RECURSOS)):
        if recursos[indice] < consumo[indice]:
            alcanza = False
    return alcanza


def simular_trayecto(recursos, dias, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True
    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            for indice in range(len(RECURSOS)):
                recursos[indice] = recursos[indice] - consumo[indice]
            dias_completados += 1
            print("Día", dias_completados,
                  "| Combustible:", recursos[COMBUSTIBLE],
                  "| Oxígeno:", recursos[OXIGENO],
                  "| Energía:", recursos[ENERGIA],
                  "| Provisiones:", recursos[PROVISIONES])
        else:
            puede_continuar = False
    return dias_completados


# ============================================================
# COMPONENTE C: EXPLORACIÓN CON BITÁCORA
# ============================================================

def mostrar_recursos(recursos):
    print("Recursos restantes:")
    for indice in range(len(RECURSOS)):
        nombre = RECURSOS[indice].capitalize()
        cantidad = recursos[indice]
        print("-", nombre + ":", cantidad, "unidades")


def mostrar_menu_actividades():
    for indice in range(len(ACTIVIDADES)):
        nombre = ACTIVIDADES[indice][ACT_NOMBRE]
        print(str(indice + 1) + ". " + nombre)
    print(str(len(ACTIVIDADES) + 1) + ". Finalizar exploración")


def explorar(recursos):
    bitacora = []
    exploracion_activa = True
    print("=== EXPLORACIÓN ===")
    while exploracion_activa:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))
        if opcion == len(ACTIVIDADES) + 1:
            print("Exploración finalizada por la tripulación.")
            exploracion_activa = False
        elif opcion >= 1 and opcion <= len(ACTIVIDADES):
            actividad = ACTIVIDADES[opcion - 1]
            combustible = actividad[ACT_COMBUSTIBLE]
            energia = actividad[ACT_ENERGIA]
            provisiones = actividad[ACT_PROVISIONES]
            if (recursos[COMBUSTIBLE] >= combustible
                    and recursos[ENERGIA] >= energia
                    and recursos[PROVISIONES] >= provisiones):
                recursos[COMBUSTIBLE] -= combustible
                recursos[ENERGIA] -= energia
                recursos[PROVISIONES] -= provisiones
                nombre = actividad[ACT_NOMBRE]
                puntos = actividad[ACT_PUNTOS]
                numero = len(bitacora) + 1
                fila = [numero, nombre, puntos]
                bitacora.append(fila)
                print("Actividad realizada: " + nombre
                      + ". Puntos obtenidos:", puntos)
            else:
                print("Recursos insuficientes para realizar la actividad. "
                      "La exploración finaliza.")
                exploracion_activa = False
        else:
            print("Opción no válida.")
    return bitacora


def contar_actividad(bitacora, nombre_actividad):
    cantidad = 0
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            cantidad += 1
    return cantidad


def calcular_puntos(bitacora):
    total_puntos = 0
    for fila in bitacora:
        total_puntos += fila[BIT_PUNTOS]
    return total_puntos


def mostrar_resumen_exploracion(bitacora, recursos):
    print("Actividades realizadas:", len(bitacora))
    muestras = contar_actividad(bitacora, "Recolectar muestra")
    print("Muestras recolectadas:", muestras)
    puntos = calcular_puntos(bitacora)
    print("Puntos científicos:", puntos)
    mostrar_recursos(recursos)


# ============================================================
# COMPONENTE D: REGRESO Y SUPERVIVENCIA
# ============================================================

def puede_regresar(recursos, dias_viaje):
    combustible_requerido = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    puede = recursos[COMBUSTIBLE] >= combustible_requerido
    return puede


def calcular_supervivencia(recursos, tripulantes):
    dias_por_recurso = []
    dias_oxigeno = recursos[OXIGENO] // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE)
    dias_energia = recursos[ENERGIA] // CONSUMO_ENERGIA_DIA
    dias_provisiones = (recursos[PROVISIONES]
                        // (tripulantes * CONSUMO_PROVISIONES_TRIPULANTE))
    dias_por_recurso.append(dias_oxigeno)
    dias_por_recurso.append(dias_energia)
    dias_por_recurso.append(dias_provisiones)
    return dias_por_recurso


def obtener_limitantes(dias_por_recurso, minimo):
    limitantes = []
    for indice in range(len(RECURSOS_VITALES)):
        if dias_por_recurso[indice] == minimo:
            limitantes.append(RECURSOS_VITALES[indice])
    return limitantes


def regresar(recursos, dias_viaje, tripulantes):
    print("=== REGRESO ===")
    if puede_regresar(recursos, dias_viaje):
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = RESULTADOS[0]
        else:
            print("El regreso se interrumpió en el día", dias_completados + 1)
            consumo = calcular_consumo_diario(tripulantes)
            for indice in range(len(RECURSOS)):
                if recursos[indice] < consumo[indice]:
                    print("Recurso insuficiente:", RECURSOS[indice])
            print("La tripulación no completó el regreso.")
            resultado = RESULTADOS[1]
    else:
        print("La tripulación quedó varada en el destino.")
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)
        for indice in range(len(RECURSOS_VITALES)):
            print("Días por", RECURSOS_VITALES[indice] + ":",
                  dias_por_recurso[indice])
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        texto_limitantes = ""
        for indice in range(len(limitantes)):
            if indice > 0:
                texto_limitantes += ", "
            texto_limitantes += limitantes[indice]
        print("Supervivencia estimada:", minimo, "días")
        print("Recurso(s) limitante(s):", texto_limitantes)
        resultado = RESULTADOS[2]
    return resultado


# ============================================================
# COMPONENTE E: REPORTE FINAL ORDENADO
# ============================================================

def obtener_puntos_actividad(fila):
    puntos = fila[BIT_PUNTOS]
    return puntos


def ordenar_bitacora(bitacora):
    bitacora_ordenada = sorted(bitacora, key=obtener_puntos_actividad,
                               reverse=True)
    return bitacora_ordenada


def mostrar_reporte(mision, bitacora):
    print("=== REPORTE FINAL ===")
    print("Misión:", mision[MIS_NOMBRE])
    print("Destino:", mision[MIS_DESTINO])
    print("Resultado:", mision[MIS_RESULTADO])
    print("Puntos científicos:", mision[MIS_PUNTOS])
    print("Bitácora de exploración (de mayor a menor puntaje):")
    if len(bitacora) == 0:
        print("Sin actividades registradas.")
    else:
        bitacora_ordenada = ordenar_bitacora(bitacora)
        for fila in bitacora_ordenada:
            print("#" + str(fila[BIT_NUMERO]), fila[BIT_ACTIVIDAD], "-",
                  fila[BIT_PUNTOS], "puntos")


# ============================================================
# COMPONENTE F: MENÚ PRINCIPAL E HISTORIAL
# ============================================================

def obtener_puntos_mision(mision):
    puntos = mision[MIS_PUNTOS]
    return puntos


def ordenar_historial(historial):
    historial_ordenado = sorted(historial, key=obtener_puntos_mision,
                                reverse=True)
    return historial_ordenado


def linea_mision(mision):
    linea = ("#" + str(mision[MIS_NUMERO]) + " "
             + mision[MIS_NOMBRE] + " | "
             + mision[MIS_DESTINO] + " | "
             + mision[MIS_RESULTADO] + " | "
             + str(mision[MIS_PUNTOS]) + " puntos")
    return linea


def mostrar_historial(historial):
    print("=== HISTORIAL DE MISIONES ===")
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        historial_ordenado = ordenar_historial(historial)
        for mision in historial_ordenado:
            print(linea_mision(mision))


def ejecutar_mision(numero):
    print("=== PLANIFICACIÓN ===")
    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))
    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))
    nombre_destino = "Ninguno"
    dias_viaje = 0
    bitacora = []
    resultado = RESULTADOS[4]

    if opcion_destino < 1 or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
    else:
        destino = DESTINOS[opcion_destino - 1]
        nombre_destino = destino[DES_NOMBRE]
        dias_viaje = destino[DES_DIAS]
        disponibles = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        mostrar_resumen(nombre_mision, nombre_destino, dias_viaje,
                        tripulantes, disponibles, requeridos)
        if autorizar_lanzamiento(disponibles, requeridos):
            print("Lanzamiento autorizado.")
            print("=== VIAJE DE IDA ===")
            recursos = viajar_al_destino(disponibles, dias_viaje, tripulantes)
            print("La nave llegó a", nombre_destino, "en", dias_viaje, "días.")
            mostrar_recursos(recursos)
            bitacora = explorar(recursos)
            mostrar_resumen_exploracion(bitacora, recursos)
            resultado = regresar(recursos, dias_viaje, tripulantes)
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
            resultado = RESULTADOS[3]

    puntos = calcular_puntos(bitacora)
    mision = [numero, nombre_mision, nombre_destino, resultado, puntos]
    mostrar_reporte(mision, bitacora)
    return mision


def mostrar_menu_principal():
    print("===== MISIÓN ÓRBITA =====")
    print("1. Planificar y ejecutar una misión")
    print("2. Ver historial de misiones")
    print("3. Salir")


def main():
    historial = []
    programa_activo = True
    while programa_activo:
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mision = ejecutar_mision(len(historial) + 1)
            historial.append(mision)
        elif opcion == 2:
            mostrar_historial(historial)
        elif opcion == 3:
            print("Fin del sistema Misión Órbita.")
            programa_activo = False
        else:
            print("Opción no válida.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================
main()
