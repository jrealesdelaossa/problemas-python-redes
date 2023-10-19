"""
Pedir al usuario que ingrese una fecha (día, mes y año) y calcular el día de la
semana correspondiente.

Toma el Domingo como el primer día de la semana.
"""


def dia_semana(dia, mes, anno):
    if mes == 1 or mes == 2:
        mes += 12
        anno -= 1

    dia_semana = (dia + 2 * mes + (3 * (mes + 1) // 5) + anno +
                  anno // 4 - anno // 100 + anno // 400 + 2) % 7

    print(f'El dia de la semana es: {dia_semana}')


# Ingreso de datos
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anno = int(input("Ingrese el año: "))

dia_semana(dia, mes, anno)
