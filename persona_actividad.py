

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
        return str("son las " + str(self.hora) + str(self.minuto) + str(self.seg) + ": ")


    def horaCorrecta(self,hr, mim, segundo):
        if str(hr).isdigit() and str(mim).isdigit() and str(segundo).isdigit():
            if 0<= hr <=23:
                if 0<= mim <=60:
                    if 0<= segundo <=60:
                        return True
                    else:
                        print("Pusiste mal los segundos")
                        return False
                else:
                    print("Pusiste mal los minutos")
                    return False
            else:
                print("Pusiste mal la hora")
                return False
        else:
            print("Tienes que ponener numeritos huevon ")
            return False



    def sethora(self,hr, mim, segundo):
        if self.horaCorrecta(hr, mim, segundo):
            self.hora = hr
            self.minuto = mim
            self.seg = segundo







