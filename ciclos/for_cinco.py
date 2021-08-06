"""
 Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""

primer_numero = int(input("ingrese un numero mayor que cero: "))

if primer_numero == 0:
    print("0 no tiene divisores.")

else:
    for contar in range(0, primer_numero):
        contar += 1
        if primer_numero % contar == 0:
            print(f"divisores {contar}")