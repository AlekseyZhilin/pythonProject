from sys import argv
from functools import reduce
from itertools import count, cycle

print("-" * 20 + "Задание1" + "-" * 20)
try:
    print("Зароботная плата сотрудника = ", float(argv[1]) * float(argv[2]) + float(argv[3]))
except ValueError:
    print("Не верно введённые параметры")
except IndexError:
    print("Не верное количество аргументов")

print("-" * 20 + "Задание2" + "-" * 20)
my_List = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_List} ")
print(f"Сгенирированный список: ", [my_List[i] for i in range(1, len(my_List)) if my_List[i - 1] < my_List[i]])

print("-" * 20 + "Задание3" + "-" * 20)
print([el for el in range(20, 241) if (el % 20 == 0 or el % 21 == 0)])

print("-" * 20 + "Задание4" + "-" * 20)
my_List = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходный список: {my_List}")
print("Сгенерированный список: ", [el for el in my_List if my_List.count(el) == 1])

print("-" * 20 + "Задание5" + "-" * 20)


def my_func(prev_el, el):
    return prev_el * el if el % 2 == 0 else prev_el


print(reduce(my_func, range(10, 101)))

print("-" * 20 + "Задание6" + "-" * 20)
it_val = int(input("Введите количество повторений: "))


def my_func_count(begin_val=int(input("Введите начальное значение: ")),
                  end_val=int(input("Введите конечное значение: "))):
    my_List = []
    for el in count(begin_val):
        if el > end_val:
            break
        else:
            my_List.append(el)

    return my_List


my_List = my_func_count()
cur_i = 0
it_val = len(my_List) * it_val - 1
for el in cycle(my_List):
    print(el, end=" ")
    cur_i += 1
    if cur_i == len(my_List):
        print()
        cur_i = 0

    if it_val == 0:
        break

    it_val -= 1

print("-" * 20 + "Задание7" + "-" * 20)


def fact(n):
    i = 1
    for cur in range(1, n + 1):
        i *= cur
        yield i


n = input("Введите целое число для получения n факториала: ")
try:
    n = int(n)
    for el in fact(n):
        print(el)
except ValueError:
    print("Неверно введённое значение")
