from evaluador.automata import *

class Evaluador:
    def __init__(self):
        self.automata = Automata()
        self.automata.estado("p", False)
        self.automata.estado("q", False)
        self.automata.estado("r", True)
        self.automata.transicion("a","#","#a","p","p")
        self.automata.transicion("b","#","#b","p","p")
        self.automata.transicion("a","a","aa","p","p")
        self.automata.transicion("b","a","ab","p","p")
        self.automata.transicion("a","b","ba","p","p")
        self.automata.transicion("b","b","bb","p","p")
        self.automata.transicion("c","#","#","p","q")
        self.automata.transicion("c","b","b","p","q")
        self.automata.transicion("c","a","a","p","q")
        self.automata.transicion("b","b","*","q","q")
        self.automata.transicion("a","a","*","q","q")
        self.automata.transicion("*","#","#","q","r")

    def evaluar(self, palabra):
        pasos = self.automata.evaluar(palabra)
        if pasos[-1]['estadoActual'] == "r":
            aceptada = True
        else:
            aceptada = False
        return [aceptada, pasos]

