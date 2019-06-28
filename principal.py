from objetos_clase1 import *
from objetos_clase2 import *
from factura import *
from empleado import *
from persona_actividad import *


#
# et = Objeto()
# print(et.color)
# print(et.tamanio)
# print(et.aspecto)
# et.color = "rosa"
# print(et.color)
#
#
#
# """objeto = MiClase()
# print objeto.propiedad
# objeto.otra_propiedad = "Nuevo valor"
# variable = objeto.metodo()
# print variable
# print objeto.otro_metodo() """
#
#
# ob = Pie()
# ob.color = "El pie de de color verde"
# ob.forma ="El pie es gordito"
# ob.amputar()
# ob.amputar()
# print("te quedaste sin deditos huevon")
# print(ob.color)
# print(ob.forma)
# print(ob.dedos)



# Prueba = Romano(950)
# print(Prueba.romanizar())



# #factura
# compra1 = Factura(12,110)
# print(compra1.unidad)
# print(compra1.precio)
# print(compra1.a_pagar(),"euros")
# print(Factura._tasas) #error
# #atribiteError:type object "factura" has no attribute "_tasa"


#empleado
# empleado1 = Empleado("Fancisco",30000)
# print(empleado1.getnombre())
# empleado1.setnombre("Francisco jose")
# print(empleado1.setnombre(),",",empleado1.getsalario())

#
# #creas una clase de personas
# nuevo_nombre = Persona()
# nuevo_nombre.nombre = "Esteban"
# nuevo_nombre.edad = 25
# print(nuevo_nombre.nombre)
# print(nuevo_nombre.edad)
# print(nuevo_nombre.corre()+ nuevo_nombre.salta()+nuevo_nombre.camina())



#reloj
relojito = Reloj()
print(relojito.dame_hora())
print(relojito.horaCorrecta(2,5,90))




