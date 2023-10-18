class circle:
    pi=3.14
    def area(self, radius):
        return circle.pi * radius **2
Circle = circle()
pizza_area = Circle.area(12 / 2)
teaching_table_area = Circle.area(36/2)
round_room_area = Circle.area(11460/2)

print(type(Circle))
print(pizza_area)
print(teaching_table_area)
print(round_room_area)

class circulo:
    pi=3.14
    def _init_(self,diameter):
    print('New circle with diameter: {}'.format(diameter))
teaching_table = circulo(36)