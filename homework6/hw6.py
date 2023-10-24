# first task
class frange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0.0
            self.stop = args[0]
            self.step = 1.0
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1.0
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise ValueError('frange() accepts 1 to 3 arguments')

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.start >= self.stop) or (self.step < 0 and self.start <= self.stop):
            raise StopIteration
        current = self.start
        self.start += self.step
        return current


for i in frange(1, 100, 3.5):
    print(i)

assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')

# second task
class Colorizer:
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    reset_code = '\033[0m'

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color in self.color_codes:
            print(self.color_codes[self.color], end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.reset_code, end='')

print('aaa')
print('bbb')
print('ccc')

with Colorizer('yellow'):
    print('printed in yellow')

print('printed in default color')
# third task
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height

class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)
c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)
p = Parallelogram(1, 2, 20, 30, 45)
p1 = Parallelogram(1, 2, 20, 30, 45)
t = Triangle(0, 0, 10, 20)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(t)

total_square = scene.total_square()
print(f'Total Square: {total_square:.3f}')