from objetos_clase1 import *
from objetos_clase2 import *
from factura import *
from empleado import *



et = Objeto()
print(et.color)
print(et.tamanio)
print(et.aspecto)
et.color = "rosa"
print(et.color)



"""objeto = MiClase()
print objeto.propiedad
objeto.otra_propiedad = "Nuevo valor"
variable = objeto.metodo()
print variable
print objeto.otro_metodo() """


ob = Pie()
ob.color = "El pie de de color verde"
ob.forma ="El pie es gordito"
ob.amputar()
ob.amputar()
print("te quedaste sin deditos huevon")
print(ob.color)
print(ob.forma)
print(ob.dedos)



Prueba = Romano(950)
print Prueba.romanizar()



#factura
compra1 = Factura(12,110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.a_pagar(),"euros")
print(Factura._tasas) #error
#atribiteError:type object "factura" has no attribute "_tasa"


#empleado
empleado1 = Empleado("Fancisco",30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco jose")
print(empleado1.setnombre(),",",empleado1.getsalario())
