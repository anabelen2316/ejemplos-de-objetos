""" El alumnado tendrá que realizar un programa que conste de una clase
llamada Alumno que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
un mensaje con el resultado de la nota y si ha aprobado o no."""

class Alumnos(object):
    nombre = ""
    nota = 0

    def get_nombre(self):
        return self.nombre
    def get_nota(self):
        return self.nota
    def set_nombre(self,apodo):
        self.nombre = apodo
    def set_nota(self,clasificacion):
        self.nota = clasificacion
    def aprobarNota(self):
        if self.nota >=5:
            print("Este alumno ha aprobado")
            return ("El Alumno ha superado el cursos, Feliz fin de Curso")







