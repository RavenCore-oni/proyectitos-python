from glob import glob
from tkinter import *
import os
from tkinter import ttk
from tkinter import Button
from tkinter import Label 
from tkinter import Entry

def factorcitobonito():
    global vent_calc
    vent_calc =Tk()    
    vent_calc.config(bg='#C4A9FF')
    vent_calc.geometry('500x300')

    global entra_fac
    global num_fact
    global resulfact
    resulfact = IntVar()
    entra_fac = IntVar()


    menubar = Menu(vent_calc)
    vent_calc.config(menu=menubar)
    salida = Menu(menubar, tearoff=0)
    salida.add_command(label = "Salir", command = vent_calc.quit)
    menubar.add_cascade(label = "Ayuda", menu = salida)

    titulo = Label(vent_calc, text='-Factorial-', bg='#C4A9FF', font=('Helvetica', 16, 'bold'))
    titulo.place(relx=0, rely=0, relwidth=1, relheight=.1)

    ingres = Label(vent_calc, text='Ingresa el numero', bg='#C4A9FF', font=('Helvetica', 14, 'bold')) 
    ingres.place(relx=.0, rely=.2, relwidth=.4, relheight=.1)

    entra_fac = Entry(vent_calc)
    entra_fac.place(relx=.5, rely=.2, relwidth=.4, relheight=.1)

    factorialcito = Label(vent_calc, text='Factorial',bg='#C4A9FF', font=('Helvetica', 14, 'bold'))
    factorialcito.place(relx=0, rely=.5, relwidth=.4, relheight=.1)

    resulfact = Entry(vent_calc)
    resulfact.place(relx=.5, rely=.5, relwidth=.4, relheight=.1)

    calcu = Button(vent_calc, text='Calcular', bg='#A9BEFF', font=('Helvetica', 14, 'bold'), command=calculopro)
    calcu.place(relx=.3, rely=.8, relwidth=.4, relheight=.1)
    vent_calc.mainloop()    

def calculopro():
    num = entra_fac.get()
    xnum = int(num)
    count = 1
    znum = 1
    while znum <= xnum:
        count = count * znum
        znum = znum + 1
    resulfact.insert(0,count)

factorcitobonito()