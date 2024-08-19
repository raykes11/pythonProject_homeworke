class Figure:
    sides_count = 0
    filled = True
    __sides = []
    __color = [0,0,0]
    def __init__(self,rgb,*new_sides):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        self.set_color(r,g,b)
        self.set_sides(*new_sides)
        if len(self.__sides)!=self.sides_count:
            cycle = 0
            while cycle < self.sides_count:
                self.__sides.append(1)
                cycle += 1


    def get_color(self):
        return self.__color
    def __is_valid_color(self,r,g,b):
        if int(r) in range(256) and int(g) in range(256) and int(b) in range(256):
            return True
        else:
            return False
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]
            return self
        else:
            return self
    def __is_valid_sides(self,*args):
        count = 0
        flag = True
        for number in args:
            number = int(number)
            if number > 0:
                count += 1
            else:
                flag = False
        if count == self.sides_count and flag:
            return True
        else:
            return False
    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = 0
        for count in self.__sides:
            P = P + count
        return P

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            return self
        else:
            return self

class Circle(Figure):
    sides_count = 1
    def __init__(self,rgb,*new_sides):
        Figure.__init__(self,rgb,*new_sides)
        self.__radius = len(self)/2/3.14
        self.__square = len(self) ** 2 / (4 * 3.14)
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return self.__square

class Triangle(Figure):
    sides_count = 3
    def __init__(self,rgb,*new_sides):
        Figure.__init__(self,rgb,*new_sides)
        A_count = self.get_sides()[0]
        B_count = self.get_sides()[1]
        C_count = self.get_sides()[2]
        p = len(self)/2
        self.__height = 2/A_count*((p*(p-A_count)*(p-B_count) *(p-C_count))**0.5)
        self.__square = ((p*(p-A_count)*(p-B_count) *(p-C_count))**0.5)
    def get_height(self):
        return self.__height
    def get_square(self):
        return self.__square

class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *new_sides):
        Figure.__init__(self, rgb, *new_sides)
        if len(new_sides) == 1:
            list_ = []
            for i in range(12):
                list_.append(new_sides[0])
            self.set_sides(*list_)
        self.__volume = self.get_sides()[0]**3
    def get_volume(self):
        return self.__volume







circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

