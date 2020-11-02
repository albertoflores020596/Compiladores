from Metodos import *
class AFN:

     def __init__(self):
        self.alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z","E","0","1","2","3","4","5","6","7","8","9"]
        self.estados_finales = list()
        self.estado_inicial = 0
        self.estados_actuales = list()
        self.transiciones = list()
        self.estados = list()
        self.estado_error = -1

     def cargar_desde(self, nombre):  # (nombre:string)
         with open('af.txt', 'r') as f:
             aut = f.read().splitlines();
         self.estado_inicial= int(aut[0])
         [self.estados_finales.append(int(s)) for s in aut[1].split(",") if s.isdigit()]
         for t in aut[2:]:
             aux=t.replace("->", ",");
             aux=aux.split(",");
             self.transiciones.append(Transicion(int(aux[0]), (aux[1]),(aux[2])))
             self.agregar_estado(aux[0])



     def guardar_en(self, nombre):  # (nombre:string)
         f = open(nombre + ".txt", 'w')
         f.write(str(self.estado_inicial) + "\n")
         for x in self.estados_finales:
             if (x)==self.estados_finales[len(self.estados_finales)-1]:
                 f.write(str(x) + "\n")
             else:
                 f.write(str(x) + ",")
         for x in self.transiciones:
             f.write(str(x.getactual())+"->"+str(x.getsiguiente())+"," +str(x.getsimbolo()))
             f.write("\n")
         f.close()

     def agregar_transicion(self, inicio, fin, simbolo):  # (inicio:int, fin:int, simbolo:char)
         self.transiciones.append(Transicion(int(inicio), int(fin), simbolo))
         self.agregar_estado(int(inicio))

     def eliminar_transicion(self, inicio, fin, simbolo):  # (inicio:int, fin:int, simbolo:char)
         cont=0;
         for t in self.transiciones:
             if str(t.getactual())==str(inicio) and str(t.getsiguiente())==str(fin) and str(t.getsimbolo())==str(simbolo):
                 break;
             cont+=1;
         self.transiciones.pop(cont);

     def obtener_inicial(self):
         return self.estado_inicial

     def obtener_finales(self):
         return self.estados_finales

     def establecer_inicial(self, estado):  # (estado:int)
         self.estado_inicial = estado;

     def establecer_final(self, estado):  # (estado:int)
         if not (str(self.estados_finales) in str(estado)):
             self.estados_finales.append(estado)

     def agregar_estado(self, estado):
         if not(estado) in self.estados:
             self.estados.add(estado)

     def acepta(self, cadena):
         self.estados_actuales = self.estados_epsilon(self.obtener_inicial())
         print(self.estados_actuales)
         for caracter in cadena:
             if caracter not in self.alfabeto:
                 return False
             siguientes_estados = self.obtener_siguientes(caracter)
             self.estados_actuales = []
             for e in siguientes_estados:
                self.estados_actuales.extend(self.estados_epsilon(e))

         for estado in self.estados_actuales:
            if estado in self.estados_finales:
                return True
         return False

     def obtener_siguientes(self, caracter):
         siguientes = list()
         for estado in self.estados_actuales:
             for transicion in self.transiciones:
                 if estado == transicion.actual and transicion.caracter == caracter:
                    siguientes.append(transicion.siguiente)
         return siguientes

     def estados_epsilon(self, estados):
         epsilon = list()
         epsilon.append(estados)
         for estado in epsilon:
             for t in self.transiciones:
                 if t.caracter == 'E' and t.actual == estado and (t.siguiente not in epsilon):
                    epsilon.append(t.siguiente)
         return epsilon