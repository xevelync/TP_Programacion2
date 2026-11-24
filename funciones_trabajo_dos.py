import random


def es_entero_positivo(texto: str) -> bool:
    """Verifica si una cadena contiene únicamente dígitos del '0' al '9'."""
    if len(texto) == 0:
        return False

    indice = 0
    while indice < len(texto):
        caracter = texto[indice]
        if caracter < "0" or caracter > "9":
            return False
        indice += 1

    return True


def leer_entero_positivo(mensaje: str) -> int:
    """Solicita un número entero positivo hasta que el ingreso sea válido."""
    while True:
        entrada = input(mensaje)
        if es_entero_positivo(entrada):
            valor = int(entrada)
            if valor > 0:
                return valor
            print("ERROR: El número debe ser mayor a 0.")
        else:
            print("ERROR: Debe ingresar un número entero válido (sin letras ni símbolos).")


def jugar_tragamonedas(puntaje_inicial: int, apuesta: int, caracteres_posibles: list) -> int:
    """Ejecuta una tirada de tragamonedas y devuelve el puntaje actualizado."""
    if puntaje_inicial <= 0:
        print("¡Perdiste todos los puntos! JUEGO TERMINADO.")
        return puntaje_inicial

    if puntaje_inicial < apuesta:
        print("PUNTAJE INSUFICIENTE. Cambie su apuesta o salga del juego.")
        return puntaje_inicial

    print("EJECUTAR TIRADA\n")

    primer_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]
    segundo_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]
    tercer_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]

    print(f"Resultados: {primer_caracter} | {segundo_caracter} | {tercer_caracter}\n")

    if primer_caracter == "0" and segundo_caracter == "0" and tercer_caracter == "0":
        puntaje_inicial = 0
        print("¡Perdiste todos los puntos acumulados!")
        print("¡JUEGO TERMINADO!\n")
    elif primer_caracter == "7" and segundo_caracter == "7" and tercer_caracter == "7":
        premio = apuesta * 10
        puntaje_inicial += premio
        print(f"¡FELICIDADES! TRIPLE 7. Ganaste {premio} puntos.\n")
    elif (
        primer_caracter == segundo_caracter
        and primer_caracter == tercer_caracter
        and (
            primer_caracter == "A"
            or primer_caracter == "B"
            or primer_caracter == "C"
            or primer_caracter == "D"
        )
    ):
        premio = apuesta * 5
        puntaje_inicial += premio
        print(f"¡Felicidades! TRES IGUALES. Ganaste {premio} puntos.\n")
    elif (
        primer_caracter == segundo_caracter
        or primer_caracter == tercer_caracter
        or segundo_caracter == tercer_caracter
    ):
        premio = apuesta * 2
        puntaje_inicial += premio
        print(f"¡Felicidades! DOS CARACTERES IGUALES. Ganaste {premio} puntos.\n")
    else:
        puntaje_inicial -= apuesta
        print(f"TODOS DISTINTOS. Suerte la próxima, perdiste {apuesta} puntos.\n")

    return puntaje_inicial


def cambiar_apuesta(puntaje_inicial: int, apuesta: int) -> int:
    """Permite modificar la apuesta actual validando que no supere el puntaje disponible."""
    print("CAMBIAR APUESTA\n")
    print(f"Tu puntaje actual es de: {puntaje_inicial}\n")
    print(f"Tu apuesta actual es de: {apuesta}\n")

    while True:
        nueva_apuesta = leer_entero_positivo("Ingresar nueva apuesta: ")
        print("")
        if nueva_apuesta > puntaje_inicial:
            print("ERROR: Tu apuesta supera el puntaje disponible. Ingresar nuevamente.")
        else:
            print(f"APUESTA CAMBIADA CORRECTAMENTE. Tu apuesta actual es: {nueva_apuesta}\n")
            return nueva_apuesta


def sumar_mano(mano: list) -> int:
    """Calcula el valor total de una mano de Blackjack ajustando Ases (11 o 1) sin usar 'in'."""
    puntaje_total = 0
    cantidad_ases = 0
    indice = 0

    while indice < len(mano):
        carta = mano[indice]
        if carta == "10" or carta == "J" or carta == "Q" or carta == "K":
            puntaje_total += 10
        elif carta == "A":
            puntaje_total += 11
            cantidad_ases += 1
        else:
            puntaje_total += int(carta)
        indice += 1

    while puntaje_total > 21 and cantidad_ases > 0:
        puntaje_total -= 10
        cantidad_ases -= 1

    return puntaje_total


def obtener_carta(mazo: list) -> str:
    """Extrae una carta aleatoria del mazo sin usar random.choice."""
    indice_carta = random.randint(0, len(mazo) - 1)
    return mazo[indice_carta]


def tomar_decision_jugador(cartas_jugador: list, mazo: list) -> list:
    """Gestiona el turno del jugador para pedir cartas o plantarse."""
    while True:
        total_jugador = sumar_mano(cartas_jugador)
        print("Tus cartas:", cartas_jugador, "| Suma total:", total_jugador)

        if total_jugador > 21:
            print("SUPERASTE LOS 21 PUNTOS.")
            break

        decision = input("[1] Pedir una carta | [2] Plantarse: ")
        print("")

        match decision:
            case "1":
                carta_nueva = obtener_carta(mazo)
                cartas_jugador = cartas_jugador + [carta_nueva]
            case "2":
                break
            case _:
                print("ERROR: Ingrese una opción correcta (1 o 2).")

    return cartas_jugador


def jugar_banca(cartas_crupier: list, mazo: list, limite: int = 17) -> list:
    """Ejecuta el turno automático de la banca hasta alcanzar el límite indicado."""
    if len(cartas_crupier) == 0:
        cartas_crupier = [obtener_carta(mazo), obtener_carta(mazo)]

    puntaje_crupier = sumar_mano(cartas_crupier)
    print("Cartas iniciales de la banca:", cartas_crupier, "| Suma total:", puntaje_crupier)

    while puntaje_crupier < limite:
        carta_nueva = obtener_carta(mazo)
        cartas_crupier = cartas_crupier + [carta_nueva]
        puntaje_crupier = sumar_mano(cartas_crupier)
        print("Cartas de la banca:", cartas_crupier, "| Suma total:", puntaje_crupier)

    return cartas_crupier


def resolver_ronda_blackjack(total_jugador: int, total_crupier: int, apuesta: int, puntaje: int) -> int:
    """Calcula ganancia o perdida de la ronda de Blackjack y actualiza el puntaje."""
    if total_jugador > 21:
        puntaje -= apuesta
        print(f"Te pasaste de 21. Perdiste {apuesta} puntos.")
    elif total_crupier > 21:
        ganancia = apuesta * 2
        puntaje += ganancia
        print(f"La banca se pasó de 21. ¡Ganaste {ganancia} puntos!")
    elif total_jugador > total_crupier:
        ganancia = apuesta * 2
        puntaje += ganancia
        print(f"¡LE GANASTE A LA BANCA! Ganaste {ganancia} puntos.")
    elif total_jugador < total_crupier:
        puntaje -= apuesta
        print(f"LA BANCA TE GANO!. Perdiste {apuesta} puntos.")
    else:
        print("EMPATE! Se mantiene tu puntaje.")

    return puntaje


def jugar_blackjack(puntaje_inicial: int, apuesta: int, mazo: list) -> int:
    """Organiza una partida completa de Blackjack y devuelve el puntaje actualizado."""
    if puntaje_inicial < apuesta:
        print("Puntaje insuficiente para apostar.")
        return puntaje_inicial

    print("MESA BLACKJACK\n")

    cartas_jugador = [obtener_carta(mazo), obtener_carta(mazo)]
    cartas_crupier = [obtener_carta(mazo), obtener_carta(mazo)]

    print("Carta visible de la banca:", cartas_crupier[0], "| Carta oculta\n")

    cartas_jugador = tomar_decision_jugador(cartas_jugador, mazo)
    total_jugador = sumar_mano(cartas_jugador)

    if total_jugador <= 21:
        cartas_crupier = jugar_banca(cartas_crupier, mazo)
        total_crupier = sumar_mano(cartas_crupier)
    else:
        total_crupier = sumar_mano(cartas_crupier)

    puntaje_inicial = resolver_ronda_blackjack(total_jugador, total_crupier, apuesta, puntaje_inicial)
    return puntaje_inicial
