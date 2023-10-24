import numpy as np

class TrianguloGeneral:
    def area(self, base, altura):
        return (base * altura)/2

trianguloGeneral = TrianguloGeneral()
area_A = trianguloGeneral.area(15,74)
print ("El área del cuadrado A es {}".format(area_A))

Dorito_A = trianguloGeneral.area(5,10)
print ("El área del dorito A es", Dorito_A)

#############################################

class TrianguloEquilatero:
    def area(self, lado):
        return ((lado ** 2) * np.sqrt(3))/4

trianguloEquilatero = TrianguloEquilatero()
area_B = trianguloEquilatero.area(119)
print ("El área del cuadrado B es {}".format(area_B))

Dorito_B = trianguloEquilatero.area(4)
print ("El área del dorito B es", Dorito_B)

#############################################

class TrianguloRectangulo:
    def area(self, base, altura):
        return (base * altura)/2

trianguloRectangulo = TrianguloRectangulo()
area_C = trianguloRectangulo.area(14, 15)
print ("El área del cuadrado C es {}".format(area_C))

Dorito_C = trianguloRectangulo.area(8, 35)
print ("El área del dorito C es", Dorito_C)