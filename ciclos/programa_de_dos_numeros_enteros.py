"""Escriba un programa que pida dos números enteros. El programa pedirá de
nuevo el segundo número mientras no sea mayor que el primero. El programa
terminará escribiendo los dos números."""

primer_numero = int(input("escriba un numero :"))
segundo_numero = int(input(f"escriba un numero mayor que {primer_numero} :"))

while segundo_numero <= primer_numero:
    segundo_numero = int(input(f"{primer_numero} no es mayor que {segundo_numero}. intentelo de nuevo :"))
else:
    print(f"muy bien {segundo_numero} es mayor que {primer_numero}")





"""
Escriba un número: 6
Escriba un número mayor que 6: 6
6 no es mayor que 6. Inténtelo de nuevo: 1
1 no es mayor que 6. Inténtelo de nuevo: 8
Los números que ha escrito son 6 y 8.
"""