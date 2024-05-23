calificacion = float(input("Digite una calificacion del 1 al 10: "))
calificacionA = calificacion >= 9 and calificacion <= 10
calificacionB = calificacion >= 8 and calificacion <= 9
calificacionC = calificacion >= 7 and calificacion <= 8
calificacionD = calificacion >= 6 and calificacion <= 7
calificacionF = calificacion >= 0 and calificacion <= 6
if calificacionA:
    print("A")
elif calificacionB:
    print("B")
elif calificacionC:
    print("C")
elif calificacionD:
    print("D")
elif calificacionF:
    print("F")
elif calificacion:
    print("De lo contrario el valor ingresado es incorrecto")

