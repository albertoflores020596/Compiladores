class Transicion:#clase transiocion para mejor manejo de las transiciones
     def __init__(self, estado, siguiente, simbolo):
         self.actual = estado
         self.siguiente = siguiente
         self.caracter = simbolo
     def __str__(self):
         return [self.actual,self.siguiente,self.caracter]
     def getactual(self):
         return self.actual
     def getsiguiente(self):
         return self.siguiente
     def getsimbolo(self):
         return self.caracter

def separar(tran): #Separa la cadena, para obtener separado  estado,estado,simbolo (quitando simbolos inecesarios)
    e=tran.replace("->",",")
    return e.split(",")