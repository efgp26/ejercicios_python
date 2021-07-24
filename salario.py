cantidad_hora = int(input("ingrese el numero de horas trabajadas: "))
valor_hora = int(input("ingrese el valor por hora trabajada en us: "))
sueldo = cantidad_hora*valor_hora
sueldo_total = (sueldo-(sueldo*4)/100)
sueldo_total_dos_porciento = (sueldo_total + ((sueldo_total*2)/100))

if sueldo_total >= 300:
    print(f"su sueldo a recibir sera:{sueldo_total} us")


else:
    print(f"su seldo a recibir sera:{sueldo_total_dos_porciento}us")
