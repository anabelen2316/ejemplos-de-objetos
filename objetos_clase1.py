



class Antena(object):
    color = ""
    longitud = ""

class Pelo(object):
    color = ""
    textura = ""

class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""

class Objeto(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

def flotar(self):
    pass

class Dedo(object):
    longitud = ""
    forma = ""
    color = ""

class Pie(object):
    forma = ""
    color = ""
    dedos = 5
    def amputar(self):
        self.dedos = self.dedos -1

# Nuevo Objeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()
    def saltar(self):
        pass



