

class Persona(object):
    edad = 0
    nombre = ""

    def corre(self):
       return ("Puede correr\n")
    def salta(self):
        return ("Puede saltar\n")
    def camina(self):
        return ("Puede caminar\n")




class Reloj(object):
    hora = 0
    minuto = 0
    seg = 0

    def dame_hora(self):
        return str("son las" + str(self.hora) + str(self.minuto) + str(self.seg) + ":")


    def horaCorrecta(self):
        if 0<= self.hora <=23 and :
            if 0<= self.minuto <=60:
                if 0<= self.seg <=60:
                    return True
        else:
            print("Pusiste mal la hora")
            return False










