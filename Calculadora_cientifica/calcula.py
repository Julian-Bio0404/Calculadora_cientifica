from math import sin, cos, tan, exp, log, log2, sqrt, radians
from tkinter import StringVar

class Calculadora:
    def __init__(self):
        self.operacion = ""
        self.resultado = 0
        self.reset_pantalla = False
        self.num1 = 0
        self.contador_resta = 0
        self.contador_multiplicar = 0
        self.contador_dividir = 0
        self.numero_pantalla = StringVar()
        
    #--------------------Pulsación_teclado--------------------#
    def numeroPulsado(self, num):
        self.num = num

        if self.reset_pantalla == True:
            self.numero_pantalla.set(self.num)
            self.reset_pantalla = False
        else:
            self.numero_pantalla.set(self.numero_pantalla.get() + self.num)

    #--------------------funcion que reinicia pantalla-------------------#
    def reinicia(self):
        self.operacion = ""
        self.resultado = 0
        self.reset_pantalla = True
        self.num1 = 0
        self.contador_resta = 0
        self.contador_multiplicar = 0

        self.numero_pantalla.set(self.resultado)

    #--------------------funcion que borra cifra en pantalla----------------------#
    def borrar(self):
        self.numero = self.numero_pantalla.get()
        self.numero_pantalla.set(self.numero[:-1])

    #--------------------funcion suma---------------------------#
    def suma(self, num):
        self.num = num
        self.resultado += float(self.num)
    
        self.numero_pantalla.set(self.entero_decimal(self.resultado))

        self.operacion = "suma"
        self.reset_pantalla = True

    #--------------------funcion resta--------------------------#
    def resta(self, num):
        self.num = num
    
        if self.contador_resta == 0:
            self.num1 = float(self.num)
            self.resultado = self.num1
        else:
            if self.contador_resta == 1:
                self.resultado = self.num1 - float(self.num)
            else:
                self.resultado = float(self.resultado) - float(self.num)

        self.numero_pantalla.set(self.entero_decimal(self.resultado))
    
        self.contador_resta += 1
        self.operacion = "resta"
        self.reset_pantalla = True

    #-----------------funcion multiplicacion---------------------#
    def multiplicar(self, num):
        self.num = num

        if self.contador_multiplicar == 0:
            self.num1 = float(self.num)
            self.resultado = self.num1
        else:
            if self.contador_multiplicar == 1:
                self.resultado = self.num1 * float(self.num)
            else:
                self.resultado = float(self.resultado) * float(self.num)
    
        self.numero_pantalla.set(self.entero_decimal(self.resultado))

        self.contador_multiplicar += 1
        self.operacion ="multiplicacion"
        self.reset_pantalla = True

    #------------------funcion dividir--------------------------------#
    def dividir(self, num):
        self.num = num

        while True:
            try:
                if self.contador_dividir == 0:
                    self.num1 = float(self.num)
                    self.resultado = self.num1 
                else:
                    if self.contador_dividir == 1:
                        self.resultado = self.num1 / float(self.num)
                    else:
                        self.resultado = float(self.resultado) / float(self.num)

                    if self.num1 % float(self.num) == 0 or float(self.resultado) % float(self.num) == 0:
                        self.numero_pantalla.set(int(self.resultado))
                    else:
                        self.numero_pantalla.set(self.resultado)
                    self.resultado = self.numero_pantalla.get()
                break
            except ZeroDivisionError:
                self.numero_pantalla.set("Math ERROR")

        self.contador_dividir += 1
        self.operacion = "division"
        self.reset_pantalla = True

    #-----------------funciones trigonometricas-----------------------#
    def aplicar_funcion(self, f, num):
        self.f = f
        self.num = num
        self.resultado = float(self.num)

        funciones = {'Sin':sin, 'Cos':cos, 'Tan':tan}

        for i,j in funciones.items():
            if self.f == i:
                self.resultado = j(radians(self.resultado))
                self.numero_pantalla.set(i + "(" + str(self.num) + ")")
                self.operacion = i

    #--------------funciones raiz cuadrada y exponencial-----------------#
    def sqrt_exponencial(self, f, num):
        self.f = f
        self.num = num
        self.resultado = float(self.num)

        funciones = {"exp": exp, "Ln":log2, "√":sqrt}

        for i,j in funciones.items():
            if self.f == i:
                self.resultado = j(self.resultado)
                self.numero_pantalla.set(i + "(" + str(self.num) + ")")
                self.operacion = i

    #------------------funcion factorial---------------------------------#
    def factorial(self, num):
        self.num = num
        self.resultado = float(self.num)
        self.resultado = int(self.resultado)

        while True:
            try:
                if self.resultado < 70:
                    for i in range(self.resultado):
                        self.resultado = self.resultado * (i + 1)
                    self.resultado = self.resultado / int(self.num)
                    self.numero_pantalla.set(int(self.resultado))
                else:
                    self.numero_pantalla.set("Math ERROR")
                break
            except ValueError:
                self.numero_pantalla.set("Math ERROR")

        self.resultado = 0
        self.reset_pantalla = True

    #-----------------funcion que devuelve decimal o entero-----------------#
    def entero_decimal(self, result):
        self.tipo_resultado = result
        #crea lista de dos elementos. 1° n antes de la coma, 2° n despues de la coma.
        self.n_next_zero = str(self.tipo_resultado).split(".")
    
        #Si el segundo elemento es diferente de "0", devolverá decimal
        if self.n_next_zero[1] != "0":
            self.tipo_resultado = float(self.tipo_resultado)
        else:
            self.tipo_resultado = int(float(self.tipo_resultado))

        return self.tipo_resultado

    #-------------------------funcion potencia-----------------------------#
    def potencia(self, num):
        self.num = num
        self.resultado = float(self.num)
        self.operacion = "potencia"
        self.reset_pantalla = True

    #------------------funcion resultado al pulsar "="---------------------#
    def el_resultado(self):

        while True:
            try:
                if self.operacion == "suma":
                    self.resultado = float(self.resultado) + float(self.numero_pantalla.get())
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))

                elif self.operacion == "resta":
                    self.resultado = float(self.resultado) - float(self.numero_pantalla.get())
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))
                    self.contador_resta = 0

                elif self.operacion == "multiplicacion":
                    self.resultado = float(self.resultado) * float(self.numero_pantalla.get())
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))
                    self.contador_multiplicar = 0

                elif self.operacion == "division":
                    if int(self.resultado) % int(self.numero_pantalla.get()) == 0:
                        self.numero_pantalla.set(int(int(self.resultado) / int(self.numero_pantalla.get())))
                    else:
                        self.numero_pantalla.set(int(self.resultado) / int(self.numero_pantalla.get()))
                    self.contador_dividir = 0

                elif self.operacion == "Sin" or self.operacion == "Cos" or self.operacion == "Tan":
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))

                elif self.operacion == "Ln" or self.operacion == "exp" or self.operacion == "√":
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))

                elif self.operacion == "potencia":
                    self.resultado = float(self.resultado) ** float(self.numero_pantalla.get())
                    self.numero_pantalla.set(self.entero_decimal(self.resultado))
                    self.resultado = 0
                break
            except ZeroDivisionError:
                self.numero_pantalla.set("Math ERROR")

        self.resultado = 0