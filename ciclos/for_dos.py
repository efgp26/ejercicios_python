"""hacer un programa que le solicite al usuario una palabra y se cuenten las vocales repetidas"""

palabra = input("ingrese una palabra: ")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0


for conteo in palabra:
    if conteo == "a":
        contador_a += 1
    elif conteo == "e":
        contador_e += 1
    elif conteo == "i":
        contador_i += 1
    elif conteo == "o":
        contador_o += 1
    elif conteo == "u":
        contador_u += 1

else:
    if contador_a > 1:
        print(f"la vocal a se repitio: {contador_a} veces")
    elif contador_e > 1:
        print(f"la vocal e se repitio {contador_e} veces")
    elif contador_i > 1:
        print(f"la vocal i se repitio {contador_i} veces")
    elif contador_o > 1:
        print(f"la vocal o se repitio {contador_o} veces")
    elif contador_u > 1:
        print(f"la vocal u se repitio {contador_u} veces")