class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))
    
class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon (RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)
    
class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

class Triangle(Polygon):
    geometric_type = 'Triangle'

    def __init__(self, sides : tuple):
        self.sides = sides
    
    def area(self,):
        a, b, c = self.sides
        p = (a+b+c)/2
        return (p * (p-a) * (p-b) * (p-c)) ** 0.5


class EquilateralTriangle(RegularPolygon, Triangle):
    geometric_type = 'Equilateral Triangle'

    def __init__(self, side):
        RegularPolygon.__init__(self, side)
        Triangle.__init__(self, (side, side, side))


hexagon = RegularHexagon(10)
print('hexagon area: {}'.format(hexagon.area()))
print('hexagon geometric type: {}'.format(hexagon.get_geometric_type()))
hexagon.plot(0.8, (75, 77))

square = Square(12)

print('square area: {}'.format(square.area()))
print('square geometric type: {}'.format(square.get_geometric_type()))
square.plot(0.93, (74, 75))

print('\nsquare mro')
for _ in square.__class__.__mro__:
    print(_)
print()
etriangle = EquilateralTriangle(1)
print('equi triangle area: {}'.format(etriangle.area()))

print('\nequi triangle mro')
for _ in etriangle.__class__.__mro__:
    print(_)
print()