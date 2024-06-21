num = int(input("Digite un numero: "))
if num < 0:
    print("El numero debe ser mayor o igual a 0")
else:
    factorial = num
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial es: {factorial}")