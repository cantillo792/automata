from tkinter import *
from tkinter import ttk
from ventana.componentes.automata import Automata
from ventana.validador import Validador
import threading
class Ventana():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("800x500")
        self.raiz.title("Automata de pila - Escuchando")
        self.automata = Automata(self.raiz)
        self.entry = Entry(self.raiz,  width=42)
        self.entry.place(x=100, y=380)
        self.validador = Validador()
        self.button = Button(self.raiz, text="Iniciar", command=lambda: self.validar())
        self.button.place(x=595, y=375)
        self.modo = IntVar()
        self.lento = Radiobutton(self.raiz, text="Lento", variable=self.modo, value=1)
        self.rapido = Radiobutton(self.raiz, text="Rapido", variable=self.modo, value=2)
        self.lento.place(x=445, y=380)
        self.rapido.place(x=515, y=380)
        self.raiz.configure(bg = "#e0e0e0")

    def validar(self):
        self.automata.actualizar(self.raiz)
        self.automata.lienzo.delete(self.automata.mensaje)
        print(self.modo)
        self.validador.validar(self.automata,self.entry.get(), self.modo.get())
