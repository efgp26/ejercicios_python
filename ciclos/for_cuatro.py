"""escriba un programa que pida dos numeros enteros y escriba que numeros son pares y cuales impares, desde
 primero hasta el segundo
 Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""

primer_numero = int(input("ingrese un numero: "))
segundo_numero = int(input("ingrese un segundo numero, debe ser mayor al anterior: "))
segundo_numero += 1

for contar in range(primer_numero, segundo_numero):
    if contar %2 == 0:
        print(f"par {contar}")
    else:
        print(f"impar {contar}")