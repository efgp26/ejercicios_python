"""Escriba un programa que pregunte cuántos números se van a introducir,
 pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero."""

cuantos_numeros = int(input("¿cuantos numeros va a introducir?: "))
numero_anterior = 0


for contar in range(0, cuantos_numeros):
    numero_anterior_dos = numero_anterior
    contar = int(input("ingresos numeros"))
    numero_anterior = contar
    if contar <= numero_anterior_dos:
        print("ingrese un numero mayor")