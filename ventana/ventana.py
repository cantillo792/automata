from tkinter import *
from tkinter import ttk
from tkthread import TkThread
from ventana.componentes.automata import Automata
from ventana.validador import Validador
import threading
class Ventana():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("800x500")
        
        self.automata = Automata(self.raiz)
        self.entry = Entry(self.raiz,  width=80)
        self.entry.pack()
        self.validador = Validador()
        self.button = Button(self.raiz, text="Validar", command=lambda: self.validar())
        self.button.pack()
        self.modo = IntVar()
        self.lento = Radiobutton(self.raiz, text="Lento", variable=self.modo, value=1)
        self.rapido = Radiobutton(self.raiz, text="Rapido", variable=self.modo, value=2)
        self.lento.pack()
        self.rapido.pack()
        self.raiz.configure(bg = "#e0e0e0")

    def validar(self):
        self.automata.actualizar(self.raiz)
        self.automata.lienzo.delete(self.automata.mensaje)
        print(self.modo)
        self.validador.validar(self.automata,self.entry.get(), self.modo.get())
