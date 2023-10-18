"""
Crear una calculadora que permita al usuario elegir una operación (suma, resta, multiplicación o división)
y realice el calculo.
"""


def suma(numero1, numero2):
    return numero1 + numero2


def resta(numero1, numero2):
    return numero1 - numero2


def multiplicacion(numero1, numero2):
    return numero1 * numero2


def divicion(numero1, numero2):
    if (numero2 == 0):
        return "No se puede dividir por 0"
    else:
        return numero1 / numero2


operation_schema = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: divicion
}


while True:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print(f'1. Suma')
    print(f'2. Resta')
    print(f'3. Multiplicación')
    print(f'4. División')
    print(f'5. Terminar')
    operacion = int(input("Seleccione la operación que desea realizar: "))

    if operacion == 5:
        break
    elif operacion != 1 or operacion != 2 or operacion != 3 or operacion != 4:
        print("Opción incorrecta")
        continue

    resultado = operation_schema.get(operacion)(numero1, numero2)

    print(f'El resultado de la operación es: {resultado}')
