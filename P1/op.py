

def separar(tran): #Separa la cadena, para obtener separado  estado,estado,simbolo (quitando simbolos inecesarios)
    e=tran.replace("->",",")
    return e.split(",")




