import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def clickMe():
    calificacion=tk.Tk()
    calificacion.title("Resultado")
    contador=0
    if nombre.get()=="Ciencia del dinero":
        texto1=ttk.Label(calificacion, text="1.- Correcta.")
        texto1.grid(column=1, row=0)
        contador=contador+1
    else:
        texto1=ttk.Label(calificacion, text="1.- Incorrecta")
        texto1.grid(column=1, row=0)
    if pregunta2.get()=="3":
        texto2=ttk.Label(calificacion, text="2.- Correcta.")
        texto2.grid(column=1, row=1)
        contador=contador+1
    else:
        texto2=ttk.Label(calificacion, text="2.- Incorrecta.")
        texto2.grid(column=1, row=1)
    if opcion.get()==1:
        texto3=ttk.Label(calificacion, text="3.- Incorrecta.")
        texto3.grid(column=1, row=2)
    elif opcion.get()==2:
        texto3=ttk.Label(calificacion, text="3.- Incorrecta.")
        texto3.grid(column=1, row=2)
    elif opcion.get()==3:
        texto3=ttk.Label(calificacion, text="3.- Correcta.")
        texto3.grid(column=1, row=2)
        contador=contador+1
    elif opcion.get()==0:
        texto3=ttk.Label(calificacion, text="3.- Incorrecta.")
        texto3.grid(column=1, row=2)
    if opcion1.get()==1:
        texto3=ttk.Label(calificacion, text="4.- Incorrecta.")
        texto3.grid(column=1, row=3)
    elif opcion1.get()==2:
        texto3=ttk.Label(calificacion, text="4.- Correcta.")
        texto3.grid(column=1, row=3)
        contador=contador+1
    elif opcion1.get()==3:
        texto3=ttk.Label(calificacion, text="4.- Incorrecta.")
        texto3.grid(column=1, row=3)
    elif opcion1.get()==0:
        texto3=ttk.Label(calificacion, text="4.- Incorrecta.")
        texto3.grid(column=1, row=3)
    if opcion_1.get()==1 or opcion_3.get()==1:
        texto5=ttk.Label(calificacion, text="5.- Correcta.")
        texto5.grid(column=1, row=4)
        contador=contador+1
    else:
        texto5=ttk.Label(calificacion, text="5.- Inorrecta.")
        texto5.grid(column=1, row=4)
    if contador==0:
        texto6=ttk.Label(calificacion, text="Calificacion=0")
        texto6.grid(column=1, row=5)
    elif contador==1:
        texto6=ttk.Label(calificacion, text="Calificacion=20")
        texto6.grid(column=1, row=5)
    elif contador==2:
        texto6=ttk.Label(calificacion, text="Calificacion=40")
        texto6.grid(column=1, row=5)
    elif contador==3:
        texto6=ttk.Label(calificacion, text="Calificacion=60")
        texto6.grid(column=1, row=5)
    elif contador==4:
        texto6=ttk.Label(calificacion, text="Calificacion=80")
        texto6.grid(column=1, row=5)
    elif contador==5:
        texto6=ttk.Label(calificacion, text="Calificacion=100")
        texto6.grid(column=1, row=5)

ventana = tk.Tk()
ventana.title("Economia")

texto=ttk.Label(ventana, text="Examen")
texto.grid(column=1, row=0)

texto1=ttk.Label(ventana, text="\n¿Que es economia?")
texto1.grid(column=0, row=1)
nombre=tk.StringVar()
nombreCapturado = ttk.Entry(ventana, width=30, textvariable=nombre)
nombreCapturado.grid(column=1, row=1)

texto1=ttk.Label(ventana, text="\n¿Cuantos tipos de economia hay?")
texto1.grid(column=0, row=2)
pregunta2=tk.StringVar()
nombreCapturado = ttk.Entry(ventana, width=12, textvariable=pregunta2)
nombreCapturado.grid(column=1, row=2)

ttk.Label(ventana, text="Economia del pais: ").grid(column=0, row=3)
opcion=tk.IntVar()
radio1=tk.Radiobutton(ventana, text="Estable", variable=opcion, value=1)
radio1.grid(column=1, row=3, sticky=tk.W)

radio2=tk.Radiobutton(ventana, text="Destruida", variable=opcion, value=2)
radio2.grid(column=2, row=3, sticky=tk.W)

radio3=tk.Radiobutton(ventana, text="Por las nubes", variable=opcion, value=3)
radio3.grid(column=3, row=3, sticky=tk.W)

ttk.Label(ventana, text="Economia del mundial: ").grid(column=0, row=4)
opcion1=tk.IntVar()
radio12=tk.Radiobutton(ventana, text="En subida", variable=opcion1, value=1)
radio12.grid(column=1, row=4, sticky=tk.W)

radio22=tk.Radiobutton(ventana, text="En bajada", variable=opcion1, value=2)
radio22.grid(column=2, row=4, sticky=tk.W)

radio32=tk.Radiobutton(ventana, text="Estable", variable=opcion1, value=3)
radio32.grid(column=3, row=4, sticky=tk.W)

ttk.Label(ventana, text="Seleccione los tipos de economia correctos:").grid(column=0, row=5)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(ventana, text="Saludable", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=1, row=5, sticky=tk.W)

opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(ventana, text="Corrupta", variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=2, row=5, sticky=tk.W)

opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(ventana, text="Especializada", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=3, row=5, sticky=tk.W)

opcion_4=tk.IntVar()
casilla_4=tk.Checkbutton(ventana, text="Inestable", variable=opcion_4)
casilla_4.deselect()
casilla_4.grid(column=4, row=5, sticky=tk.W)

opcion_5=tk.IntVar()
casilla_5=tk.Checkbutton(ventana, text="Por Prestamos", variable=opcion_5)
casilla_5.deselect()
casilla_5.grid(column=5, row=5, sticky=tk.W)

accion=ttk.Button(ventana, text="Calificar", command=clickMe)
accion.grid(column=2, row=8)

nombreCapturado.focus()

ventana.mainloop()