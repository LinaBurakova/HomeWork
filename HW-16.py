# print('Task 1')
class Figure:
    def __init__(self, name):
        self.name=name
    def get_square(self):
        return 0
    def print_square(self):
        print(f'Figure: {self.name}; square: {self.get_square()}')

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length=length
        self.width=width
        super().__init__('rectangle')

    def get_square(self):
        return self.length*self.width

class Circle(Figure):
    def __init__(self, radius):
        self.__pi = 3.14
        self.radius=radius
        super().__init__('circle')
    def get_square(self):
        return self.__pi*self.radius**2

class RightTriangle(Figure):
    def __init__(self, leg1, leg2):
        self.leg1=leg1
        self.leg2=leg2
        super().__init__('right triangle')

    def get_square(self):
            return (self.leg1 * self.leg2)/2

class Trapezoid(Figure):
    def __init__(self, base1, base2, hight):
        self.base1=base1
        self.base2=base2
        self.hight=hight
        super().__init__('trapezoid')

    def get_square(self):
            return (self.base1 + self.base2)/2*self.hight

figure1=Rectangle(20,30)
figure1.print_square()
figure2=Circle(5)
figure2.print_square()
figure3=RightTriangle(3,4)
figure3.print_square()
figure4=Trapezoid(9,7,2)
figure4.print_square()

print('Task 2')
class Figure:
    def __init__(self, name):
        self.name=name
    def __int__(self):
        return 0
    def __str__(self):
        return f'Figure: {self.name}; square: {self.__int__()}m^2'

class Rectangle(Figure):
    def __init__(self, length:int, width:int):
        self.length=length
        self.width=width
        super().__init__('rectangle')
    def __str__(self):
        return f'{super().__str__()}; length: {self.length}m; width: {self.width}m;'
    def __int__(self):
        return self.length*self.width

from math import pi
class Circle(Figure):
    def __init__(self, radius):
        self.radius=radius
        super().__init__('circle')
    def __str__(self):
        return f'{super().__str__()}; radius: {self.radius}m;'
    def __int__(self):
        return pi*self.radius**2

class RightTriangle(Figure):
    def __init__(self, leg1, leg2):
        self.leg1=leg1
        self.leg2=leg2
        super().__init__('right triangle')
    def __str__(self):
        return f'{super().__str__()}; leg1: {self.leg1}m; leg2: {self.leg2}m;'
    def __int__(self):
        return (self.leg1 * self.leg2)/2

class Trapezoid(Figure):
    def __init__(self, base1, base2, hight):
        self.base1=base1
        self.base2=base2
        self.hight=hight
        super().__init__('trapezoid')
    def __str__(self):
        return f'{super().__str__()}; base1: {self.base1}m; base2: {self.base2}m; hight: {self.hight}m;'
    def __int__(self):
        return (self.base1 + self.base2)/2*self.hight

figure1=Rectangle(20,30.5)
print(figure1)
figure2=Circle(5)
print(figure2)
figure3=RightTriangle(3,4)
print(figure3)
figure4=Trapezoid(9,7,2)
print(figure4)

print('Task 3')
class Shape:
    def __init__(self, name, x, y):
        self.name = name
        self.x=x
        self.y=y

    def Show(self):
        return f'\nFigura: {self.name}, \nInfo: point({self.x};{self.y}), '

    def Save(self, Filename: str):
        with open(Filename, 'a') as File:
            File.write(self.Show())

    def Load(self, Filename: str):
        with open(Filename, 'r') as File:
            print(File.readlines())

class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__('Square', x, y)
        self.length=length
    def Show(self):
        return super().Show()+f'length - {self.length};\n'

class Rectangle (Shape):
    def __init__(self, x, y, length, width):
        super().__init__('Rectangle', x, y)
        self.length=length
        self.width=width
    def Show(self):
        return super().Show()+f'length - {self.length}; width - {self.width};\n'

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__('Circle', x, y)
        self.radius=radius
    def Show(self):
        return super().Show() + f'radius - {self.radius};\n'

class Ellipse (Shape):
    def __init__(self, x, y, length, width):
        super().__init__('Ellipse', x, y)
        self.length = length
        self.width = width
    def Show(self):
        return super().Show() + f'length - {self.length}; width - {self.width};\n'

#создаем объекты базового класса,
# после чего с помощью цикла применяем наши методы класса Shape
sq=Square(7,8,12)
rec=Rectangle(5,6,8,5)
cir=Circle(7,7,9)
ell=Ellipse(5,5,9,6)

for i in (sq,rec,cir,ell):
    # print(i.Show())
    i.Save('text.txt')
i.Load('text.txt')







