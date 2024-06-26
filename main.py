print("Universidad Continental SGGK")
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solicitar_numero():
    while True:
        try:
            num = int(input("Ingrese un número positivo mayor que cero: "))
            if num <= 0:
                raise ValueError
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

