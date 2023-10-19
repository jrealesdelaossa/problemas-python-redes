"""
Implementar un programa que genere la secuencia de Fibonacci hasta el enésimo
término ingresado por el usuario.

La secuencia de Fibonacci es la siguiente:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
"""


# BEGIN: 7f7b7d8d3d5c
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Ingreso de datos
numero = int(input("Ingrese un número: "))

for i in range(1, numero+1):
    print(fibonacci(i))
