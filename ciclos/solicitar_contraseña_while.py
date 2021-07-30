""" Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante)
y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones."""

primer_contraseña = input("digite su contraseña")
segunda_contraseña = input("vuelva a introducir su contraseña")
contador = 1

if primer_contraseña != segunda_contraseña:
    while contador < 4:
        segunda_contraseña = input("vuelva a introducir su contraseña")
        if segunda_contraseña == primer_contraseña:
            print("fin del ciclo")
            break
        else:
            print(f"no coincide vuelva a intentar {contador} ")
        contador += 1
    else:
        print("fin del ciclo")
else:
    print("acceso permitido")

