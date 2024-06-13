suma = 0
calificacion = 0
calificacion_baja = 9999
for i in range (10):
    calificacion = float(input("Digite una diez calificaciones: "))
    suma = suma + calificacion
    i+=1
calificacion_promedio = suma/10
print("La calificacion promedio es: ", calificacion_promedio)
if calificacion <= calificacion_baja:
    calificacion_baja = calificacion
print("La calificacion mas baja es: ", calificacion_baja)