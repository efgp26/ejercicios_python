"""escriba un programa que solicite al usuario un numero, el cual se contara desde cero hasta el valor
dado por el usuario y el programa tendra que retornar los valores pares"""

numero = int(input("ingrese un numero"))

numero2 = numero + 1

for contar in range(0, numero2, 2):
    print(f"sus valores son: {contar}")

else:
    print("fin del ciclo")

