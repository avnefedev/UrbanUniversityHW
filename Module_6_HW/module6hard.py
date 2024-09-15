from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=True):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, side):
        flag = True
        for i in side:
            if i % int(i) != 0 or i < 0:
                flag = False
                break
        return flag


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, *new_sides):
        if self.sides_count == 12 and len(new_sides) == 1:
            new_sides = [new_sides[0] for _ in range(12)]
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        if len(side) == self.sides_count:
            Figure.__init__(self, side, color)
            self.__radius = side[0]/(2*pi)
        else:
            Figure.__init__(self, [1], color)
            self.__radius = 1/(2*pi)

    def get_square(self):
        return 2*pi*self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *side):
        if len(side) == self.sides_count:
            Figure.__init__(self, side, color)
        else:
            Figure.__init__(self, [1, 1, 1], color)

    def get_square(self):
        p = sum(super().get_sides())/2
        a, b, c = super().get_sides()
        return sqrt(p*(p-a)*(p-b)*(p-c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        if len(side) == 1:
            Figure.__init__(self, [side[0] for _ in range(self.sides_count)], color)
        else:
            Figure.__init__(self, [1 for _ in range(self.sides_count)], color)

    def get_volume(self):
        return super().get_sides()[0]**3







circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle = Triangle((100, 100, 100), 3, 4, 5 )
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
triangle.set_sides(4, 5, 3)  # Изменится
print(triangle.get_sides())
cube1.set_sides(10)  # Изменится
print(cube1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма и площадей:
print(cube1.get_volume())
print(circle1.get_square())
print(triangle.get_square())


