from math import inf
class Point:

    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def reflect_x(self):
        return Point(self.x, -self.y)

    def __str__(self):
        return '{}'.format((self.x, self.y))
    
    def slope_from_origin(self):
        if (self.x, self.y) == (0,0):
            return None
        if self.x == 0 and self.y != 0:
            return inf
        return self.y / self.x

    def get_line_to(self, p):
        a = (self.y - p.y)/ (self.x - p.x)
        b = self.y - a * self.x
        return (a, b)