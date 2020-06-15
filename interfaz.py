from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.resizable(0,0)
ventana.iconbitmap("D:\calcu.ico")

valor_inicial = 0

visor = Entry(ventana, font = ("Calibri 20"))
visor.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 10)

def click(valor):
    global valor_inicial
    visor.insert(valor_inicial, valor)
    valor_inicial += 1

def borrar():
    visor.delete(0, END)
    valor_inicial = 0

def operacion():
    ingresar = visor.get()
    resultado = eval(ingresar)
    visor.delete(0, END)
    visor.insert(0, resultado)
    global valor_inicial

boton_1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda:click(1))
boton_2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda:click(2))
boton_3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda:click(3))
boton_4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda:click(4))
boton_5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda:click(5))
boton_6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda:click(6))
boton_7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda:click(7))
boton_8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda:click(8))
boton_9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda:click(9))
boton_0 = Button(ventana, text = "0", width = 16, height = 2, command = lambda:click(0))

boton_borrar = Button(ventana, text = "C", width = 5, height = 2, command = lambda:borrar())
boton_punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda:click("."))

boton_suma = Button(ventana, text = "+", width = 5, height = 6, command = lambda:click("+"))
boton_resta = Button(ventana, text = "-", width = 5, height = 2, command = lambda:click("-"))
boton_multiplicacion = Button(ventana, text = "*", width = 6, height = 2, command = lambda:click("*"))
boton_division = Button(ventana, text = "/", width = 5, height = 2, command = lambda:click("/"))
boton_igual = Button(ventana, text = "=", width = 5, height = 6, command = lambda:operacion())

# Posicionamiento
# Fila 1
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_division.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_multiplicacion.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 1, column = 3, padx = 5, pady = 5)

#Fila 2
boton_7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton_8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton_9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 2, column = 3, rowspan = 2, padx = 5, pady = 5)

#Fila 3
boton_4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton_5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton_6.grid(row = 3, column = 2, padx = 5, pady = 5)

#Fila 4
boton_1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton_2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton_3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 4, column = 3, rowspan = 2, padx = 5, pady = 5)

#Fila 5
boton_0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)


ventana.mainloop()
