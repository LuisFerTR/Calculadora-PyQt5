# -*- coding: utf8 -*-
from math import sqrt


def factores_raiz(num):
    """Función que simplifica raíces cuadradas."""

    # Generamos una lista con los primeros 99 números cuadrados.
    cuadrados = [i * i for i in range(2, 100)]
    max_factor = 0

    if num < 0:
        # Si el radicando es negativo lanzamos una mensaje de error.
        return 'ERROR'

    for i in cuadrados:
        # Revisamos si num es un cuadrado entero
        if num in cuadrados:
            return int(sqrt(num))

        # Obtenemos el mayor cuadrado entero que divida
        # a num
        elif (num % i) == 0:
            max_factor = i

    if max_factor > 0:
        # Ejemplo: √32
        factor1 = max_factor  # max_factor = 16
        factor2 = num // factor1  # √16√(32/16)
        factor1 = int(sqrt(factor1))  # 4√2

        return str(factor1) + '√' + str(factor2)

    else:
        # Si no se puede simplificar la raíz devolvemos
        # la raíz cuadrada de num.
        return sqrt(num)


if __name__ == '__main__':
    print(factores_raiz(32))
    print(factores_raiz(4))
