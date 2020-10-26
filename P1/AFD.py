from op import *
class AFN:
    def __init__(self):
        self.EstadoI = list();
        self.EstadoF = list();
        self.TablaT= list();
        self.Alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def cargar_desde(self,nombre):#(nombre:string)
        with open('af.txt', 'r') as f:
            aut = f.read().splitlines();
        self.EstadoI=int(aut[0])
        self.EstadoF = [int(s) for s in aut[1].split(",")if s.isdigit()]
        for t in aut[2:]:
             self.TablaT.append(separar(t))
    def guardar_en(self,nombre):#(nombre:string)
        f = open(nombre+".txt", 'w')
        f.write(str(self.EstadoI)+"\n")
        f.write(str(self.EstadoF)+"\n")
        for x in range(0, len(self.TablaT)):
            f.write(str(self.TablaT[x][0])+"->"+str(self.TablaT[x][1])+","+str(self.TablaT[x][2]))
            f.write("\n")
        f.close()
    def agregar_transicion(self,inicio, fin,simbolo):#(inicio:int, fin:int, simbolo:char)
         self.TablaT.append([str(inicio),str(fin),str(simbolo)]);

    def eliminar_transicion(self ,inicio, fin, simbolo): #(inicio:int, fin:int, simbolo:char)
         self.TablaT.remove([str(inicio),str(fin),str(simbolo)]);

    def obtener_inicial(self):
         return self.EstadoI

    def obtener_finales(self):
         return self.EstadoF

    def establecer_inicial(self,estado):#(estado:int)
         self.EstadoI=estado

    def establecer_final(self,estado): #(estado:int)
        self.EstadoF=estado

    def esAFD(self):
        for s in self.TablaT:
            if s[3]=='E':  return False
        return True

    def esAFN(self):
         return not(esAFD())

    def acepta(self,cadena):
         ban=int(self.EstadoI)
         while ban:
             for c in cadena:
                 caminar(c)
         return
    def generar_cadena(self):
         return





