

class Persona(object):
    edad = 0
    nombre = ""

    def corre(self):
       return ("Puede correr")
    def salta(self):
        return ("Puede saltar")
    def camina(self):
        return ("Puede caminar")




class Reloj(object):
    hora = 0
    mimuto = 0
    seg = 0

    def dame_hora(self):
        return str("son las" + str(self.hora)+ str(self.mimuto)+ str(self.seg)+ ":")


    def horaCorecta(self):
        if 0<= self.hora <=23:
            if 0<= self.mimuto <=60:
                if 0<= self.seg <=60:
                    return True
        else:
            print("Pusiste mal la hora")
            return False











