"""solicitar al usuario el nombre del libro, el id, solicitar el precio, e indicar si el envio es gratis o no. Si el
envio es gratis se mostraran los datos anteriormente ingresados, y si no es gratis dira que el envio no es gratis y
enviara el nombre del libro  """

libro = input("ingrese el nombre del libro: ")
id = int(input("ingrese el numero del libro:"))
precio = float(input("ingrese el precio: "))

if precio >= 50000:
    print(f"el envio es gratis,{libro},{id},{precio}cop")

else:
    print(f"el envio no es gratis ,{libro},{id},{precio}cop")
