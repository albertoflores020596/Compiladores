from AFN import *

class Thompson:
    def __init__(self):#Inicializacion de la clase
        self.postfijo = list()
        self.transiciones = list()
        self.pila= []
        self.AFN = AFN()

    def convertir(self, ER): #metodo que recibe un Expresion regular y regresa objeto de tipo AFN
        self.convertir_postfijo(ER)
        self.generar_automata()
        return self.AFN

    def convertir_postfijo(self, cadena):#convierte ER de infijo a posfijo
        pila = []
        punto = False
        for c in cadena:
            if c == '(':
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.postfijo.append(pila.pop())
                    pila.append('.')
                    punto = False
                pila.append(c)
            elif c == ')':
                punto = True
                while len(pila) > 0 and pila[-1] != '(':
                    self.postfijo.append(pila.pop())
                try:
                    pila.pop()
                except IndexError as e:
                    raise e
            elif c == '+' or c == '*':
                self.postfijo.append(c)
            elif c == '|':
                while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*' or pila[-1] == '.'):
                    self.postfijo.append(pila.pop())
                pila.append(c)
                punto = False
            else:
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.postfijo.append(pila.pop())
                    pila.append('.')
                punto = True
                self.postfijo.append(c)

        while len(pila) > 0:
            self.postfijo.append(pila.pop())

    def generar_automata(self):#genera el automata
        inicial = 1
        final = 2
        self.AFN.alfabeto.append('E')
        for c in self.postfijo:
            if c == '*':
                s = self.pila.pop()
                self.cerradura(s, self.KLEENE)
            elif c == '+':
                s = self.pila.pop()
                self.cerradura(s, self.POSITIVA)
            elif c == '|':
                s = self.pila.pop()
                t = self.pila.pop()
                i1 = Transicion(s[1] + 1, s[0], 'E')
                i2 = Transicion(s[1] + 1, t[0], 'E')
                f1 = Transicion(s[1], s[1] + 2, 'E')
                f2 = Transicion(t[1], s[1] + 2, 'E')
                self.pila.append([s[1] + 1, s[1] + 2])
                self.transiciones.extend((i1, i2, f1, f2))
            elif c == '.':
                t = self.pila.pop()
                s = self.pila.pop()
                for aux in self.transiciones:
                    if aux.siguiente == s[1]:
                        aux.siguiente = t[0]
                self.pila.append([s[0], t[1]])
            else:
                if self.pila.__len__() > 0:
                    inicial = self.pila[-1][1] + 1
                    final = inicial + 1
                transicion = Transicion(inicial, final, c)
                self.pila.append([inicial, final])
                self.transiciones.append(transicion)
                self.AFN.alfabeto.append(c)

        self.AFN.establecer_inicial(1)
        self.AFN.establecer_final({self.pila[0][1]})
        self.AFN.transiciones = self.transiciones

    def cerradura(self, s, tipo):
        i1 = Transicion(s[1] + 1, s[0], 'E')
        s1 = Transicion(s[1], s[0], 'E')
        s2 = Transicion(s[1], s[1] + 2, 'E')
        self.pila.append([s[1] + 1, s[1] + 2])
        self.transiciones.extend((i1, s1, s2))

        if tipo == self.KLEENE:
            i2 = Transicion(s[1] + 1, s[1] + 2, 'E')
            self.transiciones.append(i2)

