from AFN import *
from AFD import *

class Subconjunto:
    def __init__(self, estados, etiqueta):
        self.estados = estados
        self.etiqueta = etiqueta

class Transformacion:
    def __init__(self, AFN):
        self.lista = list()
        self.AFN = AFN
        self.AFD = AFD()
        self.etiqueta = 'A'

    def convertir_automata(self):
        self.AFD.alfabeto = self.AFN.alfabeto
        self.AFD.alfabeto.remove('E')
        estado = self.cerradura_epsilon(self.AFN.estado_inicial)
        actual = Subconjunto(estado, self.etiqueta)
        self.lista.append(actual)
        pendientes = list()
        pendientes.append(actual)
        agregar = True
        self.etiqueta = chr(ord(self.etiqueta) + 1)
        nuevo = None
        while len(pendientes) > 0:
            actual = pendientes.pop()
            for simbolo in self.AFD.alfabeto:
                estados = self.cerradura_epsilon(self.mover(actual.estados, simbolo))
                agregar = True
                for i in self.lista:
                    if i.estados == estados:
                        agregar = False
                        nuevo = i
                        break
                if agregar:
                    nuevo = Subconjunto(estados, self.etiqueta)
                    pendientes.append(nuevo)
                    self.lista.append(nuevo)
                    self.etiqueta = chr(ord(self.etiqueta) + 1)
                self.AFD.agregar_transicion(actual.etiqueta, nuevo.etiqueta, simbolo)

        # Obtenemos los estados finales e inicial
        for elemento in self.lista:
            if self.AFN.estado_inicial in elemento.estados:
                self.AFD.estado_inicial = elemento.etiqueta
            for final in self.AFN.estados_finales:
                if final in elemento.estados:
                    self.AFD.estados_finales.add(elemento.etiqueta)

    # Operacion cerradura_epsilon
    def cerradura_epsilon(self, pila_estados):
        estados_epsilon = set()
        aux = list()
        if type(pila_estados) is set:
            aux.extend(pila_estados)
        else:
            aux.append(pila_estados)
        for estado_actual in aux:
            for t in self.AFN.transiciones:
                if t.caracter == 'e' and t.actual == estado_actual and (t.siguiente not in aux):
                    aux.append(t.siguiente)

        estados_epsilon.update(aux)
        return estados_epsilon

    # Operacion Mover
    def mover(self, estados, simbolo):
        estados_aux = set()
        for estado in estados:
            for transicion in self.AFN.transiciones:
                if simbolo != 'e' and estado == transicion.actual and transicion.caracter == simbolo:
                    estados_aux.add(transicion.siguiente)
        return estados_aux
