'''
Este es un programa simple para sacar la factorial de un numero 
usando tkinter y un par de funciones.

Espero le sirva a alguien.

Si tienes duda en algo no dudes en contactarme en instagram @ravenot.oni
no soy profesional en esto, sin embargo; puedo ayudar en algo.

'''

from tkinter import *
from tkinter import Button
from tkinter import Label 
from tkinter import Entry

def suma_matrice():
    global vent_matrice
    vent_matrice =Tk()    
    vent_matrice.config(bg='#C4A9FF')
    vent_matrice.title("Suma de dos matrices 2x2")
    vent_matrice.geometry('550x350')
    vent_matrice.resizable(0,0)

    menubar = Menu(vent_matrice)
    vent_matrice.config(menu=menubar)
    salida = Menu(menubar, tearoff=0)
    salida.add_command(label = "Salir", command = vent_matrice.quit)
    menubar.add_cascade(label = "Ayuda", menu = salida)

    global a11, a12, a21, a22
    a11 = IntVar()
    a12 = IntVar()
    a21 = IntVar()
    a22 = IntVar() 
    global b11, b12, b21, b22
    b11 = IntVar()
    b12 = IntVar()
    b21 = IntVar()
    b22 = IntVar()
    global c11, c12, c21, c22 
    c11 = IntVar()
    c12 = IntVar()
    c21 = IntVar()
    c22 = IntVar()

    titulo = Label(vent_matrice, text='- Suma de dos matrices -', bg='#C4A9FF', font=('Helvetica', 18, 'bold'))
    titulo.place(relx=0, rely=0, relwidth=1, relheight=.1)
    simbolito = Label(vent_matrice, text='+', bg='#C4A9FF', font=('Helvetica', 36, 'bold'))
    simbolito.place(x=152, y=140, width=30, height=20)
    simbolito2 = Label(vent_matrice, text='=', bg='#C4A9FF', font=('Helvetica', 36, 'bold'))
    simbolito2.place(x=345, y=140, width=30, height=20)

    matrice1 = Label(vent_matrice, text='Matriz 1', bg='#C4A9FF', font=('Helvetica', 12, 'bold'))
    matrice1.place(x=28, y=70, width=75, height=50)
    a11 = Entry(vent_matrice)
    a11.place(x=25, y=120, width=30, height=20)
    a21 = Entry(vent_matrice)
    a21.place(x=25, y=160, width=30, height=20)
    a12 = Entry(vent_matrice)
    a12.place(x=75, y=120, width=30, height=20)
    a22 = Entry(vent_matrice)
    a22.place(x=75, y=160, width=30, height=20)

    matrice2 = Label(vent_matrice, text='Matriz 2', bg='#C4A9FF', font=('Helvetica', 12, 'bold'))
    matrice2.place(x=230, y=70, width=75, height=50)
    b11 = Entry(vent_matrice)
    b11.place(x=225, y=120, width=30, height=20)
    b21 = Entry(vent_matrice)
    b21.place(x=225, y=160, width=30, height=20)
    b12 = Entry(vent_matrice)
    b12.place(x=275, y=120, width=30, height=20)
    b22 = Entry(vent_matrice)
    b22.place(x=275, y=160, width=30, height=20)

    matrice3 = Label(vent_matrice, text='Resultado', bg='#C4A9FF', font=('Helvetica', 12, 'bold'))
    matrice3.place(x=420, y=70, width=78, height=50)
    c11 = Entry(vent_matrice)
    c11.place(x=415, y=120, width=30, height=20)
    c21 = Entry(vent_matrice)
    c21.place(x=415, y=160, width=30, height=20)
    c12 = Entry(vent_matrice)
    c12.place(x=465, y=120, width=30, height=20)
    c22 = Entry(vent_matrice)
    c22.place(x=465, y=160, width=30, height=20)

    calcu = Button(vent_matrice, text='Calcular', bg='#A9BEFF', font=('Helvetica', 14, 'bold'), command=sumitamatrice_calc)
    calcu.place(relx=.3, rely=.7, relwidth=.4, relheight=.1)

    vent_matrice.mainloop()

def sumitamatrice_calc():
    num1 = a11.get()
    num2 = a12.get()
    num3 = a21.get()
    num4 = b22.get()
    num5 = b11.get()
    num7 = b12.get()
    num8 = b21.get()
    num9 = b22.get()

    z11 = int(num1) + int(num5)
    z12 = int(num2) + int(num7)
    z21 = int(num3) + int(num8)
    z22 = int(num4) + int(num9)
    
    c11.insert(0,z11)
    c12.insert(0,z12)
    c21.insert(0,z21)
    c22.insert(0,z22)

suma_matrice()
