cantidad_hora = float(input("ingrese el numero de horas trabajadas: "))
valor_hora = float(input("ingrese el valor por hora trabajada en cop: "))
sueldo = cantidad_hora*valor_hora
sueldo_total = (sueldo-(sueldo*4)/100)
sueldo_total_dos_porciento = (sueldo_total + ((sueldo_total*2)/100))

if sueldo_total >= 877803:
    print(f"su sueldo a recibir sera: ${sueldo_total}")


else:
    print(f"su seldo a recibir sera: ${sueldo_total_dos_porciento}")
