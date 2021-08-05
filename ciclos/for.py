"""escriba un programa que solicite a un usuario una palabra el programa debe decir cuantas letras
fueron ingresadas"""


"""
cadena = "jelipe"

for letra in cadena:
    if letra == "i":
        print(f"se encontro la letra {letra}")
        break
else:
    print("fin del ciclo for")
"""

"""for contador in range(1, 6):
    print(f"Valor: {contador}")"""

palabra = input("ingrese una palabra")

contador = 0

for conteo in palabra:
    print(f"su palabra es:{conteo}")
    contador += 1
else:
    print(f"su cantidad de letras es: {contador}")

