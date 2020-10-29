from abc import ABC, abstractmethod

print("-" * 20 + str("Задание1" + "-" * 20))


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for cur_str in self.matrix:
            for cur_col in cur_str:
                print(cur_col, end="\t")

            if cur_str != self.matrix[-1]:
                print()

        return ""

    def __add__(self, other):
        new_matrix = []

        if self.eq_ind(other):
            print("Размеры матриц не совпадают")
            return Matrix(self.matrix)

        for i in range(len(self.matrix)):
            my_row = []
            for j in range(len(self.matrix[0])):
                my_row.append(self.matrix[i][j] + other[i][j])
            new_matrix.append(my_row)

        return Matrix(new_matrix)

    def eq_ind(self, other):
        if len(self.matrix) != len(other):
            return True

        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other[i]) or \
                    len(self.matrix[i]) != len(self.matrix[0]):
                return True

        return False


m = Matrix([[1, 2], [3, 4], [5, 6]])
print(m + [[1, 2], [3, 4], [5, 6]])
print(m + [[1, 2], [3, 4], [5, 6], [0, 0]])
print("Сложение трёх матриц:")
print(m + [[1, 2], [3, 4], [5, 6]] + [[1, 1], [0, 0], [0, 0]])

print("-" * 20 + str("Задание2" + "-" * 20))


class Abstract_Palto(ABC):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def rashod(self):
        pass


class Abstract_Kostum(ABC):

    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def rashod(self):
        pass


class Palto(Abstract_Palto):
    def __init__(self):
        self.size = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    def rashod(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Kostum(Abstract_Kostum):
    def __init__(self):
        self.height = 0

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            self.__height = 150
        elif height > 220:
            self.__height = 220
        else:
            self.__height = height

    def rashod(self):
        return round(2 * self.__height + 0.3, 2)


p = Palto()
p.size = 10
print(f"Размер пальто: {p.size}, расход ткани: {p.rashod()}")
p.size = 70
print(f"Размер пальто: {p.size}, расход ткани: {p.rashod()}")
p.size = 50
print(f"Размер пальто: {p.size}, расход ткани: {p.rashod()}")

k = Kostum()
k.height = 100
print(f"Высота костюма: {k.height}, расход ткани: {k.rashod()}")
k.height = 250
print(f"Высота костюма: {k.height}, расход ткани: {k.rashod()}")
k.height = 200
print(f"Высота костюма: {k.height}, расход ткани: {k.rashod()}")

print("-" * 20 + str("Задание3" + "-" * 20))


class Cell():
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count >= 0:
            return Cell(self.count - other.count)
        else:
            return "Вычитание клеток не может быть выполнено"

    def __str__(self):
        return f"Количество ячеек в клетке = {self.count}"

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if other.count != 0:
            return Cell(int(self.count / other.count))
        else:
            return 0

    def make_order(self, row):
        my_row = self.count // row
        for _ in range(my_row):
            print("*" * row)
        print("*" * (self.count % row))


cell1 = Cell(2)
cell2 = Cell(3)
print("Объединение клеток: ", cell1 + cell2)
print("Вычитание клеток: ", cell1 - cell2)
print("Вычитание клеток: ", cell2 - cell1)
print("Умножение клеток: ", cell1 * cell2)
print("Деление клеток: ", cell2 / cell1)
cell3 = Cell(17)
cell3.make_order(5)

