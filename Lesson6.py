from time import sleep


print("-" * 20 + "Задание2" + "-" * 20)


class TrafficLight:
    def __init__(self):
        self.__color = ("Красный", "Жёлтый", "Зелёный")

    def running(self):
        my_time = (7, 2, 5)
        my_color = (31, 33, 32)

        for i, col in enumerate(self.__color):
            print(f"\033[{my_color[i]}m {self.__color[i]}")
            sleep(my_time[i])

        print("\033[0m {}".format("\n"))


a = TrafficLight()
a.running()

print("-" * 20 + "Задание2" + "-" * 20)


class Road:
    def __init__(self, length=5000, width=25):
        self._length = length
        self._width = width

    def get_mas(self, height=5):
        print(f"Масса асфальта для покрытия дороги: {self._length * self._width * 25 * height / 100} кг")


a = Road()
a.get_mas()

print("-" * 20 + "Задание3" + "-" * 20)


class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        try:
            print("Доход: " + str(round(float(self._income.get("wage")) + float(self._income.get("bonus")), 2)))
        except ValueError:
            print("Неверно введёные данные зарплаты")


a = Position("Aleksey", "Zhilin", "progr", 20000, 1000)
a.get_full_name()
a.get_total_income()
b = Position(input("Введите имя:"), input("Введите фамилию: "), input("Введите должность: "),
             input("Введите оклад: "), input("Введите премию: "))
b.get_full_name()
b.get_total_income()

print("-" * 20 + "Задание4" + "-" * 20)
turn_car = {"лево": "лево", "право": "право", "вперёд": "вперёд", "назад": "назад"}


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")
        self.speed = 0

    def turn(self, direction):
        print(f"Машина {self.name} повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} = {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        super(TownCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость {self.name} = {self.speed} км/ч. Превышение скорости")
        else:
            print(f"Текущая скорость {self.name} = {self.speed} км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        super(WorkCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость {self.name} = {self.speed} км/ч. Превышение скорости")
        else:
            print(f"Текущая скорость {self.name} = {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        super(SportCar, self).__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        super(PoliceCar, self).__init__(speed, color, name, is_police)


a = TownCar(40, "белый", "TownCar", False)
a.go()
a.turn(turn_car.get("лево"))
a.show_speed()
a.speed = 70
a.show_speed()
a.stop()
a.show_speed()

b = WorkCar(40, "белый", "WorkCar", False)
b.go()
b.turn(turn_car.get("право"))
b.show_speed()
b.speed = 70
b.show_speed()
b.stop()
b.show_speed()

c = PoliceCar(40, "белый", "PoliceCar")
if c.is_police:
    print("Это полицейская машина")
c.go()
c.turn(turn_car.get("право"))
c.show_speed()
c.speed = 70
c.show_speed()
c.stop()
c.show_speed()

print("-" * 20 + "Задание5" + "-" * 20)


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка ручки")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка карандаша")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка маркера")


a = Stationery("Письменная принадлежность")
a.draw()
b = Pen("Письменная принадлежность")
b.draw()
c = Pencil("Письменная принадлежность")
c.draw()
d = Handle("Письменная принадлежность")
d.draw()
