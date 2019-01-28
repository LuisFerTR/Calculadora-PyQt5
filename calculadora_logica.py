# -*- coding: utf8 -*-
# Archivo principal del proyecto.
# Falta agregar fracciones.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from calculadora_vista import *
from math import sqrt, pow
from Simplificar_raiz import factores_raiz


class MiForma(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.push0.clicked.connect(self.mostrar0)
        self.ui.push1.clicked.connect(self.mostrar1)
        self.ui.push2.clicked.connect(self.mostrar2)
        self.ui.push3.clicked.connect(self.mostrar3)
        self.ui.push4.clicked.connect(self.mostrar4)
        self.ui.push5.clicked.connect(self.mostrar5)
        self.ui.push6.clicked.connect(self.mostrar6)
        self.ui.push7.clicked.connect(self.mostrar7)
        self.ui.push8.clicked.connect(self.mostrar8)
        self.ui.push9.clicked.connect(self.mostrar9)
        self.ui.push_punto.clicked.connect(self.mostrar_punto)
        self.ui.push_negativo.clicked.connect(self.mostrar_negativo)
        self.ui.push_suma.clicked.connect(self.mostrar_suma)
        self.ui.push_resta.clicked.connect(self.mostrar_resta)
        self.ui.push_mult.clicked.connect(self.mostrar_mult)
        self.ui.push_div.clicked.connect(self.mostrar_div)
        self.ui.push_potencia.clicked.connect(self.mostrar_potencia)
        self.ui.push_raiz_cuad.clicked.connect(self.mostrar_raiz_cuad)
        self.ui.push_igual.clicked.connect(self.operacion)
        self.ui.push_bo.clicked.connect(self.borrar)
        self.ui.push_re.clicked.connect(self.reiniciar)
        self.show()

    def mostrar0(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('0')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '0')

    def mostrar1(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('1')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '1')

    def mostrar2(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('2')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '2')

    def mostrar3(self):
        if (self.ui.linea_result.text() == '0' or
                self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('3')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '3')

    def mostrar4(self):
        if (self.ui.linea_result.text() == '0' or
                self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('4')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '4')

    def mostrar5(self):
        if (self.ui.linea_result.text() == '0' or
                self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('5')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '5')

    def mostrar6(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('6')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '6')

    def mostrar7(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('7')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '7')

    def mostrar8(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('8')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '8')

    def mostrar9(self):
        if (self.ui.linea_result.text() == '0'
                or self.ui.linea_result.text() == 'ERROR'):
            self.ui.linea_result.setText('9')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '9')

    def mostrar_punto(self):
        numeros = self.ui.linea_result.text()
        punto = 0

        for i in numeros:
            if i == '.':
                punto = 1

        if numeros == '' or numeros == '0':
            self.ui.linea_result.setText('0.')

        elif punto >= 1:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '')

        else:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '.')

    def mostrar_negativo(self):
        numeros = self.ui.linea_result.text()
        negativo = 0

        for i in numeros:
            if i == '-':
                negativo = 1

        if negativo >= 1:
            self.ui.linea_result.setText(self.ui.linea_result.text() + '')

        else:
            self.ui.linea_result.setText('-' + self.ui.linea_result.text())

    def mostrar_suma(self):
        global num1
        global raiz_cuad
        global simbolo

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num1 = raiz_cuad

        else:
            num1 = float(self.ui.linea_result.text())

        simbolo = 1
        self.ui.linea_result.setText('0')

    def mostrar_resta(self):
        global num1
        global raiz_cuad
        global simbolo

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num1 = raiz_cuad

        else:
            num1 = float(self.ui.linea_result.text())
        simbolo = 2
        self.ui.linea_result.setText('0')

    def mostrar_mult(self):
        global num1
        global raiz_cuad
        global simbolo

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num1 = raiz_cuad

        else:
            num1 = float(self.ui.linea_result.text())

        simbolo = 3
        self.ui.linea_result.setText('0')

    def mostrar_div(self):
        global num1
        global raiz_cuad
        global simbolo

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num1 = raiz_cuad

        else:
            num1 = float(self.ui.linea_result.text())

        simbolo = 4
        self.ui.linea_result.setText('0')

    def mostrar_potencia(self):
        global num1
        global raiz_cuad
        global simbolo

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num1 = raiz_cuad

        else:
            num1 = float(self.ui.linea_result.text())

        simbolo = 5
        self.ui.linea_result.setText('0')

    def mostrar_raiz_cuad(self):
        global num1
        global simbolo
        global raiz_cuad
        global raiz_cuad_simplificada

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        num1 = float(self.ui.linea_result.text())

        raiz_cuad_simplificada = factores_raiz(num1)

        try:
            raiz_cuad = sqrt(num1)

            if (str(raiz_cuad)[-2] == '.' and str(raiz_cuad)[-1] == '0'):
                    self.ui.linea_result.setText(str(raiz_cuad)[:-2])

            else:
                self.ui.linea_result.setText(str(raiz_cuad))

            simbolo = 6

        except ValueError:
            self.ui.linea_result.setText('ERROR')

    def borrar(self):
        numeros = self.ui.linea_result.text()
        self.ui.linea_result.setText(numeros[:-1])

    def reiniciar(self):
        global num1
        global num2
        global simbolo

        num1 = 0
        num2 = 0
        simbolo = 0

        self.ui.linea_result.setText('0')

    def operacion(self):
        global num1
        global num2
        global simbolo
        global raiz_cuad
        global raiz_cuad_simplificada

        numeros = self.ui.linea_result.text()

        if numeros == 'ERROR':
            self.ui.linea_result.setText('0')

        elif '√' in numeros:
            num2 = raiz_cuad

        else:
            num2 = float(self.ui.linea_result.text())

        try:

            if simbolo == 1:
                suma = num1 + num2

                if (str(suma)[-2] == '.' and str(suma)[-1] == '0'):
                    self.ui.linea_result.setText(str(suma)[:-2])

                else:
                    self.ui.linea_result.setText(str(suma))

            elif simbolo == 2:
                resta = num1 - num2

                if (str(resta)[-2] == '.' and str(resta)[-1] == '0'):
                    self.ui.linea_result.setText(str(resta)[:-2])

                else:
                    self.ui.linea_result.setText(str(resta))

            elif simbolo == 3:
                mult = num1 * num2

                if (str(mult)[-2] == '.' and str(mult)[-1] == '0'):
                    self.ui.linea_result.setText(str(mult)[:-2])

                else:
                    self.ui.linea_result.setText(str(mult))

            elif simbolo == 4:
                try:
                    div = num1 / num2

                    if (isinstance(div, float) and
                            str(div)[-2] == '.' and str(div)[-1] == '0'):
                        self.ui.linea_result.setText(str(div)[:-2])
                        
                    else:
                        self.ui.linea_result.setText(str(div))

                except ZeroDivisionError:
                    self.ui.linea_result.setText('ERROR')

            elif simbolo == 5:
                potencia = pow(num1, num2)

                if (str(potencia)[-2] == '.' and str(potencia)[-1] == '0'):
                        self.ui.linea_result.setText(str(potencia)[:-2])

                else:
                    self.ui.linea_result.setText(str(potencia))

            elif simbolo == 6:
                if (str(raiz_cuad_simplificada)[-2] == '.'
                        and str(raiz_cuad_simplificada)[-1] == '0'):
                    self.ui.linea_result.setText(
                        str(raiz_cuad_simplificada)[:-2])

            else:
                self.ui.linea_result.setText(self.ui.linea_result.text())

        except NameError:
            self.ui.linea_result.setText(self.ui.linea_result.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiForma()
    w.show()
    sys.exit(app.exec_())
