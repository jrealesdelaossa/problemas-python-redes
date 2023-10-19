"""
Crear un programa que verifique la seguridad de una contraseña ingresada por el
usuario (por ejemplo, al menos 8 caracteres, una mezcla de letras, números y
símbolos, etc.).

"""
import re


def validar_contraseña(cadena):
    # Verificar que la contraseña tenga al menos 8 caracteres
    if len(cadena) < 8:
        print(f'La contraseña debe tener al menos 8 caracteres')
    else:
        # Verificar que la contraseña tenga al menos un número
        if not re.search(r'\d', cadena):
            print(f'La contraseña debe tener al menos un número')
        # Verificar que la contraseña tenga al menos una letra mayúscula
        elif not re.search(r'[A-Z]', cadena):
            print(f'La contraseña debe tener al menos una letra mayúscula')
        # Verificar que la contraseña tenga al menos una letra minúscula
        elif not re.search(r'[a-z]', cadena):
            print(f'La contraseña debe tener al menos una letra minúscula')
        # Verificar que la contraseña tenga al menos un carácter especial
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', cadena):
            print(f'La contraseña debe tener al menos un carácter especial')
        else:
            print(f'Contraseña válida')


# Ingreso de datos
contrasena = input("Ingrese una contraseña: ")
validar_contraseña(contrasena)
