# Clase Fracción
from MCD import mcd


class Fraccion:
    """Clase que emula las operaciones que
    se pueden realizar entre fracciones, números enteros
    y números reales."""

    def __init__(self, num, den):
        self.num = num
        self.den = den

        if self.den < 0:
            self.num = self.num * (-1)
            self.den = self.den * (-1)

        elif isinstance(self.num, float) or isinstance(self.den, float):
            if (str(self.num)[-2] == '.' and str(self.num)[-1] == '0'
                    and str(self.den)[-2] == '.' and str(self.den)[-1] == '0'):
                self.num = int(self.num)
                self.den = int(self.den)

    def __str__(self):

        if self.den == 0:
            return 'ERROR'

        elif self.den == 1:
            return str(self.num)

        elif isinstance(self.num, float) or isinstance(self.den, float):
            return str(self.num/self.den)

        else:
            comun = mcd(self.num, self.den)
            nuevo_num = self.num // comun
            nuevo_den = self.den // comun

            if nuevo_den == 1:
                return str(nuevo_num)

            else:
                return str(self.num // comun) + '/' + str(self.den // comun)

    def __add__(self, otro):
        """Suma de fracciones:
        a   c   ad + cb
        - + - = -------
        b   d      bd   """

        if isinstance(otro, Fraccion):
            # ad + cb
            nuevo_num = self.num * otro.den + otro.num * self.den

            # bd
            nuevo_den = self.den * otro.den

            comun = mcd(nuevo_num, nuevo_den)

            return Fraccion(nuevo_num // comun, nuevo_den // comun)

        elif isinstance(otro, float):

            nuevo_num = (self.num / self.den) + otro

            return nuevo_num

        else:
            # ad + cb
            nuevo_num = self.num + (otro * self.den)

            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __radd__(self, otro):

        if isinstance(otro, float):

            nuevo_num = (self.num / self.den) + otro

            return nuevo_num

        else:
            nuevo_num = self.num + (otro * self.den)

            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __sub__(self, otro):
        """Resta de fracciones:
        a   c   ad - cb
        - - - = -------
        b   d      bd   """

        if isinstance(otro, Fraccion):
            # ad - cb
            nuevo_num = self.num * otro.den - otro.num * self.den

            # bd
            nuevo_den = self.den * otro.den

            comun = mcd(nuevo_num, nuevo_den)

            return Fraccion(nuevo_num // comun, nuevo_den // comun)

        elif isinstance(otro, float):

            nuevo_num = (self.num / self.den) - otro

            return nuevo_num

        else:
            # ad - cb
            nuevo_num = self.num - (otro * self.den)
            # bd
            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __rsub__(self, otro):

        if isinstance(otro, float):

            nuevo_num = otro - (self.num / self.den)

            return nuevo_num

        else:

            nuevo_num = (otro * self.den) - self.num

            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __mul__(self, otro):
        """Multiplicación de fracciones:
        a   c   ac
        - * - = --
        b   d   bd   """
        if isinstance(otro, Fraccion):

            # ac
            nuevo_num = self.num * otro.num
            # bd
            nuevo_den = self.den * otro.den

            comun = mcd(nuevo_num, nuevo_den)

            return Fraccion(nuevo_num // comun, nuevo_den // comun)

        elif isinstance(otro, float):

            nuevo_num = (self.num / self.den) * otro

            return nuevo_num

        else:

            nuevo_num = self.num * otro

            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __rmul__(self, otro):

        if isinstance(otro, float):

            nuevo_num = (self.num / self.den) * otro

            return nuevo_num

        else:

            nuevo_num = self.num * otro

            comun = mcd(nuevo_num, self.den)

            return Fraccion(nuevo_num // comun, self.den // comun)

    def __truediv__(self, otro):
        """Dvisión de fracciones:
        a    c   ad
        - / - = --
        b    d   bc  """

        if isinstance(otro, Fraccion):
            # ad
            nuevo_num = self.num * otro.den
            # bc
            nuevo_den = self.den * otro.num

            comun = mcd(nuevo_num, nuevo_den)

            return Fraccion(nuevo_num // comun, nuevo_den // comun)

        elif isinstance(otro, float):

            nuevo_num = (self.num / self.den) / otro

            return nuevo_num

        else:

            nuevo_den = self.den * otro

            comun = mcd(self.num, nuevo_den)

            return Fraccion(self.num // comun, nuevo_den // comun)

    def __rtruediv__(self, otro):

        if isinstance(otro, float):

            nuevo_num = otro / (self.num / self.den)

            return nuevo_num

        else:

            nuevo_num = otro * self.den

            nuevo_den = self.num

            comun = mcd(nuevo_num, nuevo_den)

            return Fraccion(nuevo_num // comun, nuevo_den // comun)

    def __eq__(self, otro):
        """ ad = cb """

        primer_num = self.num * otro.den
        segundo_num = otro.num * self.den
        return primer_num == segundo_num

    def __lt__(self, otro):
        """ ad < cb """

        primer_num = self.num * otro.den
        segundo_num = otro.num * self.den
        return primer_num < segundo_num

    def __gt__(self, otro):
        """ ad > cb """
        primer_num = self.num * otro.den
        segundo_num = otro.num * self.den
        return primer_num > segundo_num


if __name__ == "__main__":
    frac1 = Fraccion(3.0, 4.0)
    frac2 = Fraccion(5, 6)
    frac3 = Fraccion(2, -3)
    frac4 = Fraccion(4, 6)
    frac5 = Fraccion(-2, 3)
    frac6 = Fraccion(3.2, 6.4)
    frac7 = Fraccion(3.3, 0)
    print(frac1, '+', frac2, '=', frac1 + frac2)
    print(frac1, '+', '4.4', '=', frac1 + 4.4)
    print('3', '-', frac2, '=', 3 - frac2)
    print(frac3, '*', frac1, '=', frac3 * frac1)
    print(frac1, '/', frac2, '=', frac1 / frac2)
    print(frac1, '/', '4.5', '=', frac1 / 4.5)
    print(frac3, '==', frac4, ':', frac3 == frac4)
    print(frac1, '>', frac2, ':', frac1 > frac2)
    print(5.1//4.3)
    print(4.4 + frac1)
    print(frac3 + frac5)
    print(4.0 / frac1)
    print(frac6)
    print(frac7)
    print(Fraccion(2.0, 1.0))
