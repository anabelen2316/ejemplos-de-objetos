""" Desarrollar un programa que conste de una clase padre Cuenta y
dos subclases PlazoFijo y CajaAhorro.
Definir los atributos titular y cantidad y un método para imprimir
los datos en la clase Cuenta.
La clase CajaAhorro tendrá un método para heredar los datos y
uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
Tendrá un método para obtener el importe del interés
(cantidad*interés/100) y , datos del titular, plazo, interés y total de interés.
Crear al menos un objeto de cada subclase."""



class Cuenta(object):
    titular = ""
    cantidad = 0

    def llamarCuenta(self):
       return (self.titular + str(self.cantidad))

    def get_titular(self):
        return self.titular

    def set_titular(self,valor):
        self.titular = valor

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self,x):
        self.cantidad = x


class CajaAhorro(Cuenta):
    pass


class PlazoFijo(Cuenta):
    plazo = 0
    interes = 0

    def get_plazo(self):
        return self.plazo
    def get_interes(self)
        return self.interes

    def set_plazo(self,valor1):
        self.plazo = valor1
    def set_interes(self,valor2):
        self.plazo = valor2

    def ImporteInteres(self):
        interes = self.cantidad * self.interes / 100
        return interes















