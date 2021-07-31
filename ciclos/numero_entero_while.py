""" Escriba un programa que pida números enteros mientras sean cada vez más grandes. """

primer_numero = int(input("ingrese un numero: "))
segundo_numero = int(input(f"ingrese un numero mayor a {primer_numero}: "))

while segundo_numero > primer_numero:
    primer_numero = segundo_numero
    segundo_numero = int(input(f"ingrese un numero mayor a {segundo_numero}: "))
else:
    print("fin del ciclo")









