print("Comprobamos que año es bisiesto")
opcion = 0
while opcion == 1 or opcion < 1:
 numero = float(input("Ingrese un año: "))
 if ((numero % 4 == 0) and (numero % 100 != 0) or (numero % 400 == 0)):
     print("El año es bisiesto")
 else:
     print("El año no es bisiesto")
 opcion = float(input("Para seguir adelante digite la opcion 1: "))
