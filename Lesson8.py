from abc import ABC, abstractmethod

print("-" * 20 + "Задание1" + "-" * 20)


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def to_int(cls, my_cls):
        try:
            return Data.val_month(tuple(map(int, my_cls.data.split("-"))))
        except ValueError:
            print("Неверно введённая дата")

    @staticmethod
    def val_month(my_tuple):
        if my_tuple[1] < 1 or my_tuple[1] > 12:
            print(f"Некорректно введёный месяц - {my_tuple[1]} (значение скорректировано)")
            return my_tuple[0], 1, my_tuple[2]
        return my_tuple


a = Data("31-13-2020")
print(Data.to_int(a))

print("-" * 20 + "Задание2" + "-" * 20)


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def fun_devizion(val_1, val_2):
    try:
        val_1, val_2 = map(float, (val_1, val_2))
        if val_2 == 0:
            raise MyError("Деление на ноль")
    except ValueError:
        return f"Неверно введённое число"
    except MyError as err:
        return f"{err}"
    else:
        return f"val_1 / val_2 = {round((val_1 / val_2), 2)}"


print(fun_devizion(input("Введите делимое: "), input("Введите делитель: ")))

print("-" * 20 + "Задание3" + "-" * 20)


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []


def dig_function(str1):
    str_digit = [str(i) for i in range(0, 9)]
    str_digit = "".join(str_digit) + "-."
    for i in range(len(str1)):
        if str_digit.find(str1[i - 1]) == -1:
            return True
    if str1.count("-") > 1 or str1.count(".") > 1:
        return True

    return False


while True:
    val = input("Введете число (stop - выход): ")
    if val == "stop":
        break

    try:
        if dig_function(val):
            raise MyError("Вы ввели не число")
    except MyError as err:
        print(err)
    else:
        val = float(val)
        my_list.append(val)

print(f"Введённые числа: {my_list}")

print("-" * 20 + "Задание4, 5, 6" + "-" * 20)


class Sclad:
    def __init__(self):
        self.reg_list = []
        self.pdr = []

    def add_el(self, el, col, pdr):
        self.reg_list.append({"cl": el[0], "el": el[1], "col": col, "pdr": pdr})

    def show_reg(self):
        print("-" * 78)
        print(f"{'Класс':<30} | {'Наименование':<20} | {'Кол':5} | {'Подразделение':<20}")
        print("-" * 78)
        for i in self.reg_list:
            el = [el for el in i.values()]
            print(f"{str(el[0]):<30} | {el[1]:<20} | {el[2]:5} | {self.pdr[el[3]]:<20}")

    def show_el(self, class_el):
        print("-" * 50)
        print(f"{'Наименование':<20} | {'Кол':5} | {'Подразделение':<20}")
        print("-" * 50)
        col_val = 0
        for i in self.reg_list:
            el = [el for el in i.values()]
            if el[0] == class_el[0]:
                print(f"{el[1]:<20} | {el[2]:5} | {self.pdr[el[3]]:<20}")
                col_val += el[2]
        print(f"Всего: {col_val} шт")

    def add_pdr(self, list_pdr):
        self.pdr = list_pdr


class Podrazdeleniy:
    def __init__(self, *pdr):
        self.my_list = list(pdr)

    def my_pdr(self):
        return self.my_list

    def add_pdr(self, pdr):
        if not (pdr in self.my_list):
            self.my_list.append(pdr)

    def ret_pdr(self, pdr):
        self.add_pdr(pdr)
        return self.my_list.index(pdr)


class Orgtehnica(ABC):
    def __init__(self, name):
        self.name = name

    def ret_data(self):
        return self.__class__, self.name

    @abstractmethod
    def change_elem(self):
        pass


class Printer(Orgtehnica):
    def __init__(self, name):
        super().__init__(name)
        self.change_elem()

    def change_elem(self):
        self.name += ", printer"


class Scanner(Orgtehnica):
    def __init__(self, name):
        super().__init__(name)
        self.change_elem()

    def change_elem(self):
        self.name += ", scanner"


class Xerox(Orgtehnica):
    def __init__(self, name):
        super().__init__(name)
        self.change_elem()

    def change_elem(self):
        self.name += ", xerox"


skl = Sclad()
my_pdr = Podrazdeleniy("Подразделение1", "Подразделение2")
a = Printer("Printer")
b = Printer("Printer 2")
c = Scanner("Scanner")
d = Xerox("Xerox")
skl.add_el(a.ret_data(), 5, my_pdr.ret_pdr("Подразделение1"))
skl.add_el(b.ret_data(), 6, my_pdr.ret_pdr("Подразделение1"))
skl.add_el(c.ret_data(), 7, my_pdr.ret_pdr("Подразделение2"))
skl.add_el(d.ret_data(), 8, my_pdr.ret_pdr("Подразделение3"))
skl.add_pdr(my_pdr.my_pdr())
print("Количество оргтехники на складе")
skl.show_reg()
print("Количество принтеров на складе")
skl.show_el(a.ret_data())

print("-" * 20 + "Задание7" + "-" * 20)


class ComplexVal:
    def __init__(self, val_cmp):
        self.val_cmp = complex(val_cmp)

    def __add__(self, other):
        return ComplexVal(complex(self.val_cmp.real + other.val_cmp.real, self.val_cmp.imag + other.val_cmp.imag))

    def __mul__(self, other):
        return ComplexVal(complex(self.val_cmp.real * other.val_cmp.real - self.val_cmp.imag * other.val_cmp.imag,
                                  self.val_cmp.real * other.val_cmp.imag + other.val_cmp.real * self.val_cmp.imag))

    def __str__(self):
        return f"{complex(self.val_cmp)}"


a = ComplexVal(3 + 1j)
b = ComplexVal(2 - 3j)
print(a.val_cmp)
print(b.val_cmp)
print("a + b = ", a + b)
print("a * b = ", a * b)
