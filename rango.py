"""solicitar al usuario un valor para calcular e identificar si este esta en el rango de 0 a 5"""

valor = int(input("ingrese un valor de 0 a 5: "))

if(valor >= 0) and (valor <= 5):
    print(f"valor en rango")
else:
    print("valor fuera de rango")
