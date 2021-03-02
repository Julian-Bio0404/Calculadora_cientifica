from tkinter import Frame, Entry, Tk, Button, StringVar

root = Tk()
frame1 = Frame(root)
frame1.pack()

operacion = ""
resultado = 0
reset_pantalla = False
num1 = 0

#---------------------pantalla------------------------------#
numero_pantalla = StringVar()
pantalla = Entry(frame1, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------------Pulsación_teclado--------------------#
def numeroPulsado(num):
    global reset_pantalla

    if reset_pantalla == True:
        numero_pantalla.set(num)
        reset_pantalla = False
    else:
        numero_pantalla.set(numero_pantalla.get() + num)

#--------------------funcion que reinicia-------------------#
def reinicia():
    global resultado
    global reset_pantalla
    resultado = 0
    reset_pantalla = True
    numero_pantalla.set(resultado)

#--------------------funcion que borra----------------------#
def borrar():
    numero = numero_pantalla.get()
    numero_pantalla.set(numero[:-1])

#--------------------funcion suma---------------------------#
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado += float(num)
    
    numero_pantalla.set(entero_decimal(resultado))

    operacion = "suma"
    reset_pantalla = True

#--------------------funcion resta--------------------------#
contador_resta = 0
def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    global contador_resta
    global num1
    
    if contador_resta == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - float(num)
        else:
            resultado = float(resultado) - float(num)

    numero_pantalla.set(entero_decimal(resultado))
    resultado = numero_pantalla.get()

    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True

#-----------------funcion multiplicacion---------------------#
contador_multiplicar = 0
def multiplicar(num):
    global operacion
    global resultado
    global reset_pantalla
    global contador_multiplicar
    global num1

    if contador_multiplicar == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_multiplicar == 1:
            resultado = num1 * float(num)
        else:
            resultado = float(resultado) * float(num)
    
    numero_pantalla.set(entero_decimal(resultado))
    resultado = numero_pantalla.get()

    contador_multiplicar += 1
    operacion ="multiplicacion"
    reset_pantalla = True

#------------------funcion dividir--------------------------------#
contador_dividir = 0
def dividir(num):
    global operacion
    global resultado
    global reset_pantalla
    global contador_dividir
    global num1

    while True:
        try:
            if contador_dividir == 0:
                num1 = float(num)
                resultado = num1 
            else:
                if contador_dividir == 1:
                    resultado = num1 / float(num)
                else:
                    resultado = float(resultado) / float(num)

                if num1 % float(num) == 0 or float(resultado) % float(num) == 0:
                    numero_pantalla.set(int(resultado))
                else:
                    numero_pantalla.set(resultado)
                resultado = numero_pantalla.get()
            break
        except ZeroDivisionError:
            numero_pantalla.set("Math ERROR")

    contador_dividir += 1
    operacion = "division"
    reset_pantalla = True

#-----------------funcion que devuelve decimal o entero-----------------#
def entero_decimal(result):
    tipo_resultado = result
    n_next_zero = str(tipo_resultado).split(".")
    
    if len(n_next_zero[1]) > 1 or n_next_zero[1] != "0":
        tipo_resultado = float(tipo_resultado)
    elif len(n_next_zero[1]) == 1:
        tipo_resultado = int(float(tipo_resultado))

    return tipo_resultado

#------------------funcion resultado al pulsar "="---------------------#
def el_resultado():
    global operacion
    global resultado
    global contador_resta
    global contador_multiplicar
    global contador_dividir

    while True:
        try:

            if operacion == "suma":
                numero_pantalla.set(entero_decimal(resultado) + int(numero_pantalla.get()))
                resultado = 0

            elif operacion == "resta":
                resultado = float(resultado) - float(numero_pantalla.get())
                numero_pantalla.set(entero_decimal(resultado))
                contador_resta = 0
                resultado = 0

            elif operacion == "multiplicacion":
                resultado = float(resultado) * float(numero_pantalla.get())
                numero_pantalla.set(entero_decimal(resultado))
                resultado = 0
                contador_multiplicar = 0

            elif operacion == "division":
                if int(resultado) % int(numero_pantalla.get()) == 0:
                    numero_pantalla.set(int(int(resultado) / int(numero_pantalla.get())))
                else:
                    numero_pantalla.set(int(resultado) / int(numero_pantalla.get()))
            break

        except ZeroDivisionError:
            numero_pantalla.set("Math ERROR")

    resultado = 0
    contador_dividir = 0

#-----------------------------botones fila1----------------------------------#
boton7 = Button(frame1, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(frame1, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(frame1, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(frame1, text="/", width=3, command=lambda:dividir(numero_pantalla.get()))
botonDiv.grid(row=2, column=4)

#-----------------------------botones fila2----------------------------------#
boton4 = Button(frame1, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(frame1, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(frame1, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonX = Button(frame1, text="X", width=3, command=lambda:multiplicar(numero_pantalla.get()))
botonX.grid(row=3, column=4)

#-----------------------------botones fila3----------------------------------#
boton1 = Button(frame1, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(frame1, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(frame1, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(frame1, text="-", width=3, command=lambda:resta(numero_pantalla.get()))
botonRest.grid(row=4, column=4)

#-----------------------------botones fila4----------------------------------#
boton0 = Button(frame1, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(frame1, text=".", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(frame1, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(frame1, text="+", width=3, command=lambda:suma(numero_pantalla.get()))
botonSum.grid(row=5, column=4)

#-----------------------------botones fila5----------------------------------#
botonac = Button(frame1, text="AC", width=3, command=lambda:reinicia())
botonac.grid(row=6, column=1)
botonDEL = Button(frame1, text="DEL", width=3, command=lambda:borrar())
botonDEL.grid(row=6, column=2)


root.mainloop()