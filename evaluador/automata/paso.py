from grafo.grafo import Grafo, Nodo
from automata.estado import Estado
from automata.pila import Pila

class Paso:
    def __init__(self, estadoActual, posCinta, pila):
        self.estadoActual = estadoActual.getValor()
        self.posCinta = posCinta
        self.pila = str(pila)
        self.transicion = ""
    def setTransicion(self, transicion):
        self.transicion = transicion
    def __str__(self):
        return "estado: "+str(self.estadoActual)+"\nposición cinta: "+str(self.posCinta)+"\npila: "+str(self.pila)+"\ntransición: "+str(self.transicion)