tarifa = float(input("Introduce la tarifa por hora: "))
horas = int(input("Introduce las horas trabajadas: "))


# Calculamos las horas extras si las hay
if horas > 40:
    extras = horas - 40
    horas = 40
else:
    extras = 0
salario_normal = tarifa * horas
if extras > 0:
    salario_extra = (tarifa * 1.5) * extras
    salario_total = salario_normal + salario_extra
else:
    salario_total = salario_normal


print("El salario total es: $ ", salario_total)