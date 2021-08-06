"""En este apartado se pretende escribir un programa que simule un
juego similar al juego de cartas "Las siete y media". En vez de pedir
cartas, los jugadores tirarán unos dados cuantas veces quieran y el valor
límite es el 20 (gana el que obtiene la puntuación más alta sin superar el límite).
"""
"""Amplíe el programa anterior, haciendo que el programa muestre la suma de los números anteriores."""

"""3 - Amplíe el programa anterior creando dos jugadores que tiran sus dados simultáneamente. El programa 
declarará ganador al jugador que haya obtenido más puntos."""

""" """

import random

suma1 = 0
suma2 = 0
jugador1 = (input("jugador1:¿desea tirar los dados?: "))
jugador2 = (input("jugador2:¿desea tirar los dados?: "))

while jugador1 == "si" and jugador2 == "si":
    dado1 = random.randint(1, 6)
    suma1 += dado1
    dado2 = random.randint(1, 6)
    suma2 += dado2
    print(f"jugador 1 su dado es: {dado1} . sus puntos son: {suma1}. "
          f"jugador 2 su dado es: {dado2}, sus puntos son:{suma2}")
    if (suma1 > 20) or (suma2 > 20):
        jugador1 = "no"
        jugador2 = "no"
    elif (suma1 <= 20) or (suma2 <= 20):
        jugador1 = (input("jugador1:¿desea volver a tirar los dados?: "))
        jugador2 = (input("jugador2:¿desea volver a tirar los dados?: "))

else:
    jugador1 = suma1
    jugador2 = suma2
    if jugador1 == jugador2:
        print("empate")
    else:
        if (jugador1 > 20) and (jugador2 > 20):
            print("los dos han perdido")
        elif jugador1 > 20:
            print("jugador 2 haz ganado")
        elif jugador2 > 20:
            print("jugador 1 haz ganado")
        elif jugador1 > jugador2:
            print("jugador 1 haz ganado, ")
        else:
            print("jugador 2 haz ganado")


"""    if jugador1 == jugador2:
        print(han quedado enpatados")
    elif jugador1 and jugador2 > 20 :
        print("los dos han perdido")
    elif jugador1 > 20:
        print("jugador 1 haz perdido")
    elif jugador2 > 20:
        print("jugador 2 haz perdido")

    else:
        if jugador1 > jugador2:
            print("jugador 1 haz ganado, ")
        else:
            print("jugador 2 haz ganado")
"""












"""Escriba un programa que muestre números al azar del 1 al 6 mientras lo pida el usuario. """