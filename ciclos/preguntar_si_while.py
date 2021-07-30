"""escriba un programa que pregunte una y otra vez al usuario si desea continuar
siempre que se conteste si en minuscula"""

# 1- solicitar datos al usuario
# 2- si el usuario da un valor diferente a si
# 3- volver apreguntar el valor solicitado
# 4- si el valor es falso fin del ciclo

continuar = input("digite si para continuar: ")

while continuar == "si":
    continuar = input("¿desea continuar?")
else:
    print("fin del ciclo")




