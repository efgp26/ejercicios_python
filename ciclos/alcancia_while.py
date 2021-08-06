"""Escriba un programa que simule una alcancia. El programa solicitará primero una cantidad, que será
la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las
cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
"""
cantidad_ahorrar = float(input("¿cual es la cantidad de dinero que desea ahorrar?: "))
ahorrado = 0
contador = 0

while contador < cantidad_ahorrar:
    ahorrado = float(input("¿cuanto va a meter en la alcancia?: "))
    contador += ahorrado

else:
    print(f"felicitaciones ya cumpliste tu meta de ahorrar {cantidad_ahorrar}. haz ahorrado {contador}")
