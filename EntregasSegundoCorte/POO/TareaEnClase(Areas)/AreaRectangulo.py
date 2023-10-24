class Rectangulo:
    def area(self, altura, base):
        return base * altura

rectangulo = Rectangulo()
area = rectangulo.area(9,13)
print ("El área del rectángulo es {}".format(area))

Escritorio = rectangulo.area(128,52)
print ("El área del ecritorio es", Escritorio, "cm")