import funciones_trabajo_dos as f

puntaje_inicial = 100
apuesta = 10
jugar = True

caracteres_posibles = ["A", "B", "C", "D", "E", "0", "7"]
mazo = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

while jugar and puntaje_inicial > 0:
    print("¡BIENVENIDOS A NUESTRO JUEGO!")
    print("")
    print(f"Tu puntaje es de: {puntaje_inicial} y tu apuesta actual de: {apuesta}")
    print("")
    print("Menú de opciones:")
    print("1. Jugar Tragamonedas")
    print("2. Jugar BlackJack")
    print("3. Cambiar apuesta")
    print("4. Salir")
    print("")
    menu = f.pedir_entero("Elegí una opción del menú: ")
    print("")

    match menu:
        case 1:
            puntaje_inicial = f.jugar_tragamonedas(puntaje_inicial, apuesta, caracteres_posibles)
        case 2:
            puntaje_inicial = f.jugar_blackjack(puntaje_inicial, apuesta, mazo)
        case 3:
            apuesta = f.cambiar_apuesta(puntaje_inicial, apuesta)
        case 4:
            print(f"Gracias por jugar! Tu puntaje es {puntaje_inicial}")
            jugar = False
        case _:
            print("Opción inválida.")
            print("")

if puntaje_inicial <= 0 and jugar:
    print("TE QUEDASTE SIN PUNTOS!")
