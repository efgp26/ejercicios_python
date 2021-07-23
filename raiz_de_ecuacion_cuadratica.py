import math


valor1 = float(input("ingrese a: "))
valor2 = float(input("ingrese b: "))
valor3 = float(input("ingrese c: "))
 
ecuacion = ((-valor2) + math.sqrt((valor2**2) - 4*(valor1*valor3))) / (2*valor1)
ecuacion2 = ((-valor2) - math.sqrt((valor2**2) - 4*(valor1*valor3))) / (2*valor1)
print(f"el primer resultado es:{ecuacion}  el segundo resultado es: {ecuacion2}")
