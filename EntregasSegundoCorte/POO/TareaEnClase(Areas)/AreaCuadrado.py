class Cuadrado:
    def area(self, lado):
        return lado ** 2

cuadrado = Cuadrado()
area = cuadrado.area(15)
print ("El área del cuadrado A es {} cm".format(area))

Lienzo = cuadrado.area(26)
print ("El área del lienzo es", Lienzo, "cm")