from evaluador.automata.transicion import Transicion
class Estado:
    
    def __init__(self, valor, final):
        self.valor = valor
        self.transiciones = []
        self.final = final
    
    def addTransicion(self, valor, simbolo, tope, agregar, destino):
        self.transiciones.append(Transicion(valor, simbolo, tope, agregar, destino))
    
    def getValor(self):
        return self.valor
    
    def getTransiciones(self):
        return self.transiciones
    
    def esFinal(self):
        return self.final

    def buscarTransicion(self, simbolo, tope):
        for t in self.transiciones:
            if t.simbolo == simbolo and t.tope == tope:
                return t
        return None

    def __str__(self):
        return self.valor