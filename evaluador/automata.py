from evaluador.estado import Estado
from evaluador.pila import Pila

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

class Automata():
    def __init__(self):
        self.estados = []
        self.palabra = []
        self.pila = Pila()
        self.pila.incluir("#")

    def estado(self, valor, final):
        self.estados.append(Estado(valor, final))

    def buscar(self, valor):
        for estado in self.estados:
            if estado.getValor() == valor:
                return estado

    def getEstados(self):
        return self.estados

    def transicion(self, simbolo, tope, agregar,  valorOrigen, valorDestino):
        origen = self.buscar(valorOrigen)
        destino = self.buscar(valorDestino)
        if origen is not None and destino is not None:
            origen.addTransicion(None, simbolo, tope, agregar, destino)
        else:
            raise Exception("Alguno de los nodos no existe")

    def llenarpila(self, elementos):
        for elem in elementos:
            if elem == "*":
                pass
            else:
                self.pila.incluir(elem)

    def __Evaluar(self, estado, pospalabra, pasos):
        if estado.esFinal() == True:
            paso = Paso(estado, pospalabra, self.pila)
            pasos.append(paso.__dict__)
        else:
            paso = Paso(estado, pospalabra, self.pila)
            transicion = estado.buscarTransicion(self.palabra[pospalabra], self.pila.inspeccionar())
            if transicion is not None:
                paso.setTransicion(transicion.dict)
                self.pila.extraer()
                self.llenarpila(transicion.agregar)
                pasos.append(paso.__dict__)
                return self.__Evaluar(transicion.destino, pospalabra+1, pasos)
            pasos.append(paso.__dict__)
        return pasos

    def evaluar(self, palabra):
        pasos = []
        for letra in palabra:
            self.palabra.append(letra)
        self.palabra.append("*")
        return self.__Evaluar(self.estados[0], 0, pasos)
