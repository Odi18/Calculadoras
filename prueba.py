from tkinter import *

ventana = Tk()
ventana.title("Calculadora Cientifica")
ventana.resizable(0,0)
ventana.configure(bg = "#002E3D")

caja_texto = Entry(ventana, font = "Calibri 19")
caja_texto.grid(row = "0", column = "0", columnspan = "5", padx = 5, pady = 10)

caja_resultado = Entry(ventana, font= "Calibiri 25")
caja_resultado.grid(row = "0", column = "5", columnspan = "5", rowspan = "10", padx = 5, pady = 10)

contador = 0

def pulsar(teclado):
    global contador
    caja_texto.insert(contador, teclado)
    contador += 1

def borrar_todo():
    caja_texto.delete(0, END)
    global contador

def operacion():
    operaciones = caja_texto.get()
    resultado = eval(operaciones)
    caja_texto.delete(0, END)
    caja_texto.insert(0, resultado)
    global contador
    
    caja_resultado.insert(contador, resultado)
    contador += 1
    
# 1era fila
boton_DEG = Button(ventana, text = "DEG", width = "5", height = "2", bg = "#005C7A")
boton_F_E = Button(ventana, text = "F-E", width = "5", height = "2", bg = "#005C7A")

# 2da fila
boton_MC = Button(ventana, text = "MC", width = "5", height = "2", bg = "#005C7A")
boton_MR = Button(ventana, text = "MR", width = "5", height = "2", bg = "#005C7A")
boton_M_mas = Button(ventana, text = "M+", width = "5", height = "2", bg = "#005C7A")
boton_M_menos = Button(ventana, text = "M-", width = "5", height = "2", bg = "#005C7A")
boton_MS = Button(ventana, text = "MS", width = "5", height = "2", bg = "#005C7A")

# 3ra fila
boton_trigonometria = Button(ventana, text = "◣ Trigonometría", width = "13", height = "2", bg = "#00A8E0")
boton_funcion = Button(ventana, text = "ƒ Función", width = "13", height = "2", bg = "#00A8E0")

# 4ta fila
boton_2nd = Button(ventana, text = "2nd", width = "5", height = "2", bg = "#008CBA")
boton_pi = Button(ventana, text = "π", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("3.1416"))
boton_e = Button(ventana, text = "e", width = "5", height = "2", bg = "#008CBA")
boton_CE = Button(ventana, text = "CE", width = "5", height = "2", bg = "#008CBA", command = lambda: borrar_todo())
boton_Borrar = Button(ventana, text = "←", width = "5", height = "2", bg = "#005C7A")

# 5ta fila
boton_x2 = Button(ventana, text = "x²", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("**2"))
boton_1sobrex = Button(ventana, text = "¹/x", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("1/"))
boton_valorabsoluto = Button(ventana, text = "|x|", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("|"))
boton_exp = Button(ventana, text = "exp", width = "5", height = "2", bg = "#008CBA")
boton_mod = Button(ventana, text = "mod", width = "5", height = "2", bg = "#008CBA")

# 6ta fila
boton_x3 = Button(ventana, text = "x³", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("**3"))
boton_parentesis_abrir = Button(ventana, text = "(", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("("))
boton_parentesis_cerrar = Button(ventana, text = ")", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar(")"))
boton_factorial = Button(ventana, text = "n!", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("!"))
boton_division = Button(ventana, text = "÷", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("/"))

# 7ma fila
boton_x_a_la_y = Button(ventana, text = "x^y", width = "5", height = "2", bg = "#008CBA")
boton_7 = Button(ventana, text = "7", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(7))
boton_8 = Button(ventana, text = "8", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(8))
boton_9 = Button(ventana, text = "9", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(9))
boton_multiplicacion = Button(ventana, text = "x", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("*"))

# 8va fila
boton_10_a_la_x = Button(ventana, text = "10^x", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("10**"))
boton_4 = Button(ventana, text = "4", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(4))
boton_5 = Button(ventana, text = "5", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(5))
boton_6 = Button(ventana, text = "6", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(6))
boton_resta = Button(ventana, text = "-", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("-"))

# 9na fila
boton_log = Button(ventana, text = "log", width = "5", height = "2", bg = "#008CBA")
boton_1 = Button(ventana, text = "1", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(1))
boton_2 = Button(ventana, text = "2", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(2))
boton_3 = Button(ventana, text = "3", width = "5", height = "2", bg = "#00BBFA", command = lambda: pulsar(3))
boton_suma = Button(ventana, text = "+", width = "5", height = "2", bg = "#008CBA", command = lambda: pulsar("+"))

#10ma fila
boton_ln = Button(ventana, text = "ln", width = "5", height = "2", bg = "#008CBA")
boton_0 = Button(ventana, text = "0", width = "13", height = "2", bg = "#00BBFA", command = lambda: pulsa(0))
boton_punto = Button(ventana, text = ".", width = "5", height = "2",  bg = "#005C7A", command = lambda: pulsar("."))
boton_igual = Button(ventana, text = "=", width = "5", height = "2", bg = "#008CBA", command = lambda:operacion())

# METODO GRID

boton_DEG.grid(row = "1", column = "0", padx = 5, pady = 2)
boton_F_E.grid(row = "1", column = "1", padx = 5, pady = 2)

boton_MC.grid(row = "2", column = "0", padx = 5, pady = 2)
boton_MR.grid(row = "2", column = "1", padx = 5, pady = 2)
boton_M_mas.grid(row = "2", column = "2", padx = 5, pady = 2)
boton_M_menos.grid(row = "2", column = "3", padx = 5, pady = 2)
boton_MS.grid(row = "2", column = "4", padx = 5, pady = 2)

boton_trigonometria.grid(row = "3", column = "0", columnspan = "2", padx = 5, pady = 2)
boton_funcion.grid(row = "3", column = "2", columnspan = "2", padx = 5, pady = 2)

boton_2nd.grid(row = "4", column = "0", padx = 5, pady = 2)
boton_pi.grid(row = "4", column = "1", padx = 5, pady = 2)
boton_e.grid(row = "4", column = "2", padx = 5, pady = 2)
boton_CE.grid(row = "4", column = "3", padx = 5, pady = 2)
boton_Borrar.grid(row = "4", column = "4", padx = 5, pady = 2)

boton_x2.grid(row = "5", column = "0", padx = 5, pady = 2)
boton_1sobrex.grid(row = "5", column = "1", padx = 5, pady = 2)
boton_valorabsoluto.grid(row = "5", column = "2", padx = 5, pady = 2)
boton_exp.grid(row = "5", column = "3", padx = 5, pady = 2)
boton_mod.grid(row = "5", column = "4", padx = 5, pady = 2)

boton_x3.grid(row = "6", column = "0", padx = 5, pady = 2)
boton_parentesis_abrir.grid(row = "6", column = "1", padx = 5, pady = 2)
boton_parentesis_cerrar.grid(row = "6", column = "2", padx = 5, pady = 2)
boton_factorial.grid(row = "6", column = "3", padx = 5, pady = 2)
boton_division.grid(row = "6", column = "4", padx = 5, pady = 2)

boton_x_a_la_y.grid(row = "7", column = "0", padx = 5, pady = 2)
boton_7.grid(row = "7", column = "1", padx = 5, pady = 2)
boton_8.grid(row = "7", column = "2", padx = 5, pady = 2)
boton_9.grid(row = "7", column = "3", padx = 5, pady = 2)
boton_multiplicacion.grid(row = "7", column = "4", padx = 5, pady = 2)

boton_10_a_la_x.grid(row = "8", column = "0", padx = 5, pady = 2)
boton_4.grid(row = "8", column = "1", padx = 5, pady = 2)
boton_5.grid(row = "8", column = "2", padx = 5, pady = 2)
boton_6.grid(row = "8", column = "3", padx = 5, pady = 2)
boton_resta.grid(row = "8", column = "4", padx = 5, pady = 2)

boton_log.grid(row = "9", column = "0", padx = 5, pady = 2)
boton_1.grid(row = "9", column = "1", padx = 5, pady = 2)
boton_2.grid(row = "9", column = "2", padx = 5, pady = 2)
boton_3.grid(row = "9", column = "3", padx = 5, pady = 2)
boton_suma.grid(row = "9", column = "4", padx = 5, pady = 2)

boton_ln.grid(row = "10", column = "0", padx = 5, pady = 2)
boton_0.grid(row = "10", column = "1", columnspan = "2", padx = 5, pady = 2)
boton_punto.grid(row = "10", column = "3", padx = 5, pady = 2)
boton_igual.grid(row = "10", column = "4", padx = 5, pady = 2)


ventana.mainloop()
