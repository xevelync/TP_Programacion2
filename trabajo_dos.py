import funciones_trabajo_dos as f

puntaje_inicial = 100
apuesta = 10
jugar = True
caracteres_posibles = ["A", "B", "C", "D", "E", "0", "7"]
mazo = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

while jugar and puntaje_inicial > 0:
    print("¡BIENVENIDOS A NUESTRO JUEGO!\n")
    print(f"Tu puntaje inicial es de: {puntaje_inicial} y tu apuesta actual es de: {apuesta}\n")
    print("Menú de opciones:")
    print("1. Jugar Tragamonedas")
    print("2. Jugar BlackJack")
    print("3. Cambiar apuesta")
    print("4. Salir\n")

    opcion = leer_entero_positivo("Elegí una opción del menú: ")
    print("")

    match opcion:
        case 1:
            puntaje_inicial = jugar_tragamonedas(puntaje_inicial, apuesta, caracteres_posibles)
        case 2:
            puntaje_inicial = jugar_blackjack(puntaje_inicial, apuesta, mazo)
        case 3:
            apuesta = cambiar_apuesta(puntaje_inicial, apuesta)
        case 4:
            print(f"GRACIAS POR JUGAR. Te retiras con un total de {puntaje_inicial} puntos.")
            jugar = False
        case _:
            print("OPCIÓN INVÁLIDA. Por favor, intente nuevamente.")

    if puntaje_inicial <= 0 and jugar:
        print("Te quedaste sin puntos! JUEGO TERMINADO.")
        jugar = False
