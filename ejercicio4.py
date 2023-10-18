"""
Pedir al usuario que ingrese dos valores y luego intercambiar los valors de las variables
y mostrarlos
"""

valor_a = input("Ingrese el primer valor: ")
valor_b = input("Ingrese el segundo valor: ")

print(f'Valor A: {valor_a}')
print(f'Valor B: {valor_b}')

auxiliar = valor_a

valor_a = valor_b
valor_b = auxiliar

print(f'Nuevo valor A: {valor_a}')
print(f'Nuevo valor B: {valor_b}')
