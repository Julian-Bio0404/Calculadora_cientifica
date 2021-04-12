from tkinter import Frame, Entry, Tk, Button, StringVar
from calcula import Calculadora

root = Tk()
frame2 = Frame(root)
frame2.pack()
ca = Calculadora()

#---------------------pantalla------------------------------#
pantalla = Entry(frame2, textvariable=ca.numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#-----------------------------botones fila1----------------------------------#
boton_raiz = Button(frame2, text="√", width=3, command=lambda:ca.sqrt_exponencial("√", ca.numero_pantalla.get()))
boton_raiz.grid(row=2, column=1)
boton_exp = Button(frame2, text="e", width=3, command=lambda:ca.sqrt_exponencial("exp", ca.numero_pantalla.get()))
boton_exp.grid(row=2, column=2)
boton_log = Button(frame2, text="log", width=3, command=lambda:ca.sqrt_exponencial("log", ca.numero_pantalla.get()))
boton_log.grid(row=2, column=3)
boton_ln = Button(frame2, text="Ln", width=3, command=lambda:ca.aplicar_funcion("Ln", ca.numero_pantalla.get()))
boton_ln.grid(row=2, column=4)

#-----------------------------botones fila2----------------------------------#
boton_sin = Button(frame2, text="Sin", width=3, command=lambda:ca.aplicar_funcion("Sin", ca.numero_pantalla.get()))
boton_sin.grid(row=3, column=1)
boton_cos = Button(frame2, text="Cos", width=3, command=lambda:ca.aplicar_funcion("Cos", ca.numero_pantalla.get()))
boton_cos.grid(row=3, column=2)
boton_tan = Button(frame2, text="Tan", width=3, command=lambda:ca.aplicar_funcion("Tan", ca.numero_pantalla.get()))
boton_tan.grid(row=3, column=3)
boton_fac = Button(frame2, text="!", width=3, command=lambda:ca.factorial(ca.numero_pantalla.get()))
boton_fac.grid(row=3, column=4)

#-----------------------------botones fila3----------------------------------#
boton7 = Button(frame2, text="7", width=3, command=lambda:ca.numeroPulsado("7"))
boton7.grid(row=4, column=1)
boton8 = Button(frame2, text="8", width=3, command=lambda:ca.numeroPulsado("8"))
boton8.grid(row=4, column=2)
boton9 = Button(frame2, text="9", width=3, command=lambda:ca.numeroPulsado("9"))
boton9.grid(row=4, column=3)
botonDiv = Button(frame2, text="/", width=3, command=lambda:ca.dividir(ca.numero_pantalla.get()))
botonDiv.grid(row=4, column=4)

#-----------------------------botones fila4----------------------------------#
boton4 = Button(frame2, text="4", width=3, command=lambda:ca.numeroPulsado("4"))
boton4.grid(row=5, column=1)
boton5 = Button(frame2, text="5", width=3, command=lambda:ca.numeroPulsado("5"))
boton5.grid(row=5, column=2)
boton6 = Button(frame2, text="6", width=3, command=lambda:ca.numeroPulsado("6"))
boton6.grid(row=5, column=3)
botonX = Button(frame2, text="X", width=3, command=lambda:ca.multiplicar(ca.numero_pantalla.get()))
botonX.grid(row=5, column=4)

#-----------------------------botones fila5----------------------------------#
boton1 = Button(frame2, text="1", width=3, command=lambda:ca.numeroPulsado("1"))
boton1.grid(row=6, column=1)
boton2 = Button(frame2, text="2", width=3, command=lambda:ca.numeroPulsado("2"))
boton2.grid(row=6, column=2)
boton3 = Button(frame2, text="3", width=3, command=lambda:ca.numeroPulsado("3"))
boton3.grid(row=6, column=3)
botonRest = Button(frame2, text="-", width=3, command=lambda:ca.resta(ca.numero_pantalla.get()))
botonRest.grid(row=6, column=4)

#-----------------------------botones fila6----------------------------------#
boton0 = Button(frame2, text="0", width=3, command=lambda:ca.numeroPulsado("0"))
boton0.grid(row=7, column=1)
botonComa = Button(frame2, text=".", width=3, command=lambda:ca.numeroPulsado("."))
botonComa.grid(row=7, column=2)
botonIgual = Button(frame2, text="=", width=3, command=lambda:ca.el_resultado())
botonIgual.grid(row=7, column=3)
botonSum = Button(frame2, text="+", width=3, command=lambda:ca.suma(ca.numero_pantalla.get()))
botonSum.grid(row=7, column=4)

#-----------------------------botones fila7----------------------------------#
botonac = Button(frame2, text="AC", width=3, command=lambda:ca.reinicia())
botonac.grid(row=8, column=1)
botonDEL = Button(frame2, text="DEL", width=3, command=lambda:ca.borrar())
botonDEL.grid(row=8, column=2)
boton_potencia = Button(frame2, text="^", width=3, command=lambda:ca.potencia(ca.numero_pantalla.get()))
boton_potencia.grid(row=8, column=4)

root.mainloop()