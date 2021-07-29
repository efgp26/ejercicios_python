"""solicitar al usuario su edad e identificar si el usuario se enentra en el rango de 20 a 29 años o el usuario
se encuentra dentro de la edad 30 a 39, si la persona se encuentra en el rango de 20 años imprimir la edad y
decir que se encuentra dentro del rango de 20 años, y si se encuentra en el rango de 30 años decir que se encuentra
dentro del rango."""

edad = int(input("ingrese su edad: "))

if (edad >= 20) and (edad <= 29):
    print(f"{edad} se encuentra en el rango de 20 años")

elif (edad >= 30) and (edad <= 39):
    print(f"{edad} se encuentra en el rango de 30 años")

else:
    print("edad fuera de rango")