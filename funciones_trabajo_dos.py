import random  

def jugar_tragamodenas(puntaje_incial, apuesta, caracteres_posibles):
    """"Documentacion
    """
    if puntaje_inicial >= apuesta:
        print("EJECUTAR TIRADA")
        print("")

        primer_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]
        segundo_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]
        tercer_caracter = caracteres_posibles[random.randint(0, len(caracteres_posibles) - 1)]

        print(f"Resultados: {primer_caracter} | {segundo_caracter} | {tercer_caracter}")
        print("")

        if primer_caracter == "0" and segundo_caracter == "0" and tercer_caracter == "0":
            puntaje_inicial = 0
            print(f"¡Perdiste todos los puntos acumulado!")
            print("¡JUEGO TERMINADO!")
            print("")

        elif primer_caracter == "7" and segundo_caracter == "7" and tercer_caracter == "7":
            puntos_ganados = apuesta * 10
            puntaje_inicial += puntos_ganados
            print(f"FELICIDADES! TRIPLE 7. Ganaste {puntos_ganados} puntos!")
            print("")

        elif primer_caracter == segundo_caracter and primer_caracter == tercer_caracter and (primer_caracter == "A" or primer_caracter == "B" or primer_caracter == "C" or primer_caracter == "D"):
            puntos_ganados = apuesta * 5
            puntaje_inicial += puntos_ganados
            print(f"Felicidades! TRES IGUALES. Ganaste {puntos_ganados} puntos!.")
            print("")

        elif primer_caracter == segundo_caracter or primer_caracter == tercer_caracter or segundo_caracter == tercer_caracter:
            puntos_ganados = apuesta * 2
            puntaje_inicial += puntos_ganados
            print(f"Felicidades! DOS CARACTERES IGUALES. Ganaste {puntos_ganados} puntos!.")
            print("")

        else:
            puntaje_inicial -= apuesta
            print(f"TODOS DISTINTOS! Suerte la proxima, perdiste {apuesta} puntos.")
            print("")

    elif puntaje_inicial == 0:
        print("Perdiste todos los puntos! JUEGO TERMINADO!!")

    else:
        print("PUNTAJE INSUFICINTE. Ingresar nueva apuesta o salir del juego")

def cambiar_apuesta(puntaje_inicial:int, apuesta:int):
    """Documentacion
    """
    print("CAMBIAR APUESTA")
    print("")
    print(f"Tu puntaje actual es de: {puntaje_inicial}")
    print("")
    print(f"Tu apuesta actual es de: {apuesta}")
    print("")

    cambiar_apuesta = True

    while cambiar_apuesta == True:
        nueva_apuesta = int(input("Ingresar nueva apuesta: "))
        print("")

        if nueva_apuesta < 1:
            print("ERROR! Tu apuesta debe ser mayor a 0. Ingresar nuevamente.")

        elif nueva_apuesta > puntaje_inicial:
            print("ERROR! Tu apuesta supera el tu puntaje disponible. Ingresar nuevamente.")
        
        elif nueva_apuesta > 0 and nueva_apuesta <= puntaje_inicial:
            apuesta = nueva_apuesta
            print(f"APUESTA CAMBIADA CORRECTAMENTE! Tu apuesta actual es: {apuesta}")
            print("")
            break

        else:
            print("ERROR. Igrese un numero entero VALIDO!")

def sumar_mano(mano:list) -> int:
    """Documentacion
    """

    puntaje_total = 0
    cantidad_ases = 0

    for carta in mano:
        if carta == "10" or carta == "J" or carta == "Q" or carta == "K":
            puntaje_total += 10
        elif carta == "A":
            puntaje_total += 11
            cantidad_ases += 1
        else:
            total += int(carta)

    while puntaje_total > 21 and cantidad_ases > 0:
        total -= 10
        cantidad_ases += 1

    return total

def obtener_carta(mazo:list):
    """Documentacion
    """
    carta_extraida = random.randint(0, len(mazo)-1)
    return mazo[carta_extraida]

def tomar_decision_jugador(mano_jugador:list, mazo:list)->list:
    """Documentacion
    """
    jugar = True
    while jugar:
        total_puntaje_jugador = sumar_mano(mano_jugador)
        print("Tus cartas:", mano_jugador, " | Suma total:", total_puntaje_jugador)

        if total_puntaje_jugador > 21:
            print("SUPERASTE LOS 21 PUNTOS")
            break

        decision = input("[1] Pedir una carta | [2] Plantarse")
        print("")

        match decision:
            case "1":
                carta_nueva = obtener_carta(mazo)
                mano_jugador += [carta_nueva]
            case "2":
                jugar = False
            case _:
                print("ERROR! Ingrese una opcion correcta.")

    return mano_jugador

def jugar_banca(mano_banca: list, mazo:list)-> list:
    """Documentacion
    """
    banca_mano = [obtener_carta(mazo), obtener_carta(mazo)]
    puntaje_total_banca = sumar_mano(banca_mano)

    while puntaje_total_banca < 17:
        carta_nueva_banca = obtener_carta(mazo)
        mano_banca = banca_mano + [carta_nueva_banca]
        puntaje_total_banca = sumar_mano(banca_mano)
        print("Cartas de la banca:", mano_banca, "| Suma total:", puntaje_total_banca)

    return banca_mano

def jugar_blackjack(puntaje_inicial:int, apuesta: int, mazo: list)-> int:
    """Documentacion
    """
    if puntaje_inicial < apuesta:
        print("Puntaje insuficiente.")

    print("MESA BLACKJACK")

    mano_jugador = [obtener_carta(mazo), obtener_carta(mazo)]
    mano_banca = [obtener_carta(mazo), obtener_carta(mazo)]

    print("Carta visible:", mano_banca[0], "| Carta oculta")

    mano_jugador = tomar_decision_jugador(mano_jugador, mazo)
    puntaje_total_jugador = sumar_mano(mano_jugador)
    mano_banca = jugar_banca(mano_banca, mazo)
    puntaje_total_banca = sumar_mano(mano_banca)


    if puntaje_total_jugador > 21:
        puntaje_inicial -= apuesta
        print("Te pasaste.")
    elif puntaje_total_banca > 21:
        puntos_ganados = apuesta * 2
        puntaje_inicial += puntos_ganados
        print("La banca se paso.")
    elif puntaje_total_jugador > puntaje_total_banca:
        puntos_ganados = apuesta * 2
        puntaje_inicial += puntos_ganados
        print("Le ganaste a la banca.")
    elif puntaje_total_jugador < puntaje_total_banca:
        puntaje_inicial -= apuesta
        print("La banca te gano")
    else:
        print("Empate")

    return puntaje_inicial

