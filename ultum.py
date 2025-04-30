# Pide al usuario un número entero
n = int(input("Ingrese un número entero: "))

# Crea una matriz cuadrada de "n" filas y "n" columnas
macua = [[f"{pri}-{seg}" for seg in range(1, n+1)] for pri in range(1, n+1)]

print((macua))