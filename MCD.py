# Algoritmo de Euclides para Máximo Común Divisor


def mcd(m, n):
    """Algoritmo de Euclides para obtener el
     Máximo Común Divisor de dos números."""

    while m % n != 0:

        m_viejo = m
        n_viejo = n

        m = n_viejo
        n = m_viejo % n_viejo

    return n
