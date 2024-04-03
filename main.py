print("Universidad Continental SGGK")
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para solicitar un número positivo mayor que cero
def solicitar_numero():
    while True:
        try:
            num = input("Ingrese un número positivo mayor que cero: ")
            num = int(num)
            if num <= 0:
                raise ValueError("El número debe ser positivo y mayor que cero.")
            return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Solicitar entrada de los números al usuario
num1 = solicitar_numero()
num2 = solicitar_numero()

# Calcular el MCD utilizando la función
mcd = calcular_mcd(num1, num2)

# Mostrar el resultado
print("El MCD de", num1, "y", num2, "es:", mcd)

