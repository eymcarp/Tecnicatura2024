'''
miVariable = 3
print(miVariable)
print(id(miVariable))

a = False
print(type(a))
# ID para ver las literales y los valores de las variables
# print para imprimir el codigo
# Type para mostrar el tipo de dato, int, float, string o bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de Cadenas (STRING)

miGrupoFavorito = "AC/DC"
caracteristicas = "La mejor banda de rock"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = 7
numero2 = 8
print(int(numero1) + int(numero2))

# Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
resultado = input("Digite un numero: ") #REGRESA UN DATO TIPO STRING
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma: int = operandoA + operandoB
#print("Resultado de la suma:",suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es:{division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo(modulo) es:{modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es:{exponente}")
"""
"""
alto = int(input("Proporciona el alto del rectangulo:"))
ancho = int(input("Proporciona el ancho del rectangulo:"))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area:",area)
print("Perimetro:",perimetro)
"""
""""
miVariable3 = 10
print(miVariable3)
#Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
""
miVariable3 += 1
print(miVariable3)

#mivariable3 = miVariable3 - 2
miVariable3 -=2
print(miVariable3)
#mivariable3 = miVariable3 * 3
miVariable3 *=3
print(miVariable3)

#mivariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

#Operadores de comparacion
d = 4
b = 2
resultado = d == b
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#operador mayor que
resultado = d > b
print(resultado)

#operador menor que
resultado = d < b
print(resultado)
#operador menor o igual que
resultado = d <= b
print(resultado)
#operador mayor o igual que
resultado = d >= b
print(resultado)
"""
#OPERADORES LOGICOS
a = False
b = False
resultado = a and b
print(resultado)
#Operador or
resultado = a or b
print(resultado)
#Operador not
resultado = not a
print(resultado)







