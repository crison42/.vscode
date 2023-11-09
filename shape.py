from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def getPerimeter(self):
        return self.a + self.b + self.c


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b

    def getPerimeter(self):
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def getArea(self):
        return 3.14 * self.r * self.r

    def getPerimeter(self):
        return 2 * 3.14 * self.r


def pull():
    a1 = eval(input("请输入三角形边长a1:"))

    a2 = eval(input("请输入三角形边长a2:"))

    a3 = eval(input("请输入三角形边长a3:"))
    if a1 + a2 > a3 and a2 + a3 > a1 and a1 + a3 > a2:
        return a1, a2, a3
    else:
        print("输入的三边长不能构成三角形")
        return pull()


a1, a2, a3 = pull()

t1 = Triangle(a1, a2, a3)

print(f"三角形面积={t1.getArea()}")

print(f"三角形周长={t1.getPerimeter()}")

b1 = eval(input("请输入矩形边长b1:"))

b2 = eval(input("请输入矩形边长b2:"))

r1 = Rectangle(b1, b2)

print(f"矩形面积={r1.getArea()}")

print(f"矩形周长={r1.getPerimeter()}")

r1 = eval(input("请输入圆的半径r1:"))

c1 = Circle(r1)

print(f"圆面积={c1.getArea()}")

print(f"圆周长={c1.getPerimeter()}")
