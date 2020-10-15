def zagolovok(n):
    print("-" * 20 + "Задание" + n + "-" * 20)


zagolovok("1")


def my_del_arg(arg_1, arg_2):
    try:
        arg_1 = float(arg_1)
        arg_2 = float(arg_2)
    except ValueError:
        print("Неверно введёные аргументы")
        return None

    if arg_2 != 0:
        return arg_1 / arg_2
    else:
        print("Деление на ноль")
        return None


print("Результат деления: ", my_del_arg(input("Введите делимое: "), input("Введите делитель: ")))

zagolovok("2")


def data_polz(name, famil, year, town, email, tel):
    return f"name: {name}, famil: {famil}, year: {town}, email: {email}, tel: {tel}"


def data_polz2(**kwargs):
    return kwargs


print(data_polz(name="Aleksey", famil="Zhilin", year=1980, town="Pokrov", email="email@email.ru", tel="111-111-11-11"))
# Второй вариант
print(data_polz2(name="Aleksey", famil="Zhilin", year=1980, town="Pokrov", email="email@email.ru", tel="111-111-11-11"))

zagolovok("3")


def my_func(arg_1, arg_2, arg_3):
    return sum([arg_1, arg_2, arg_3]) - min(arg_1, arg_2, arg_3)


print("Сумма двух наибольших аргументов: ", my_func(1, 2.2, 3.3))

zagolovok("4")


def my_func(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Неверно введённые значения (str)")
        return None

    if x == 0 or y == 0:
        print("Деление на 0")
    elif x < 0:
        print("x < 0")
    elif y > 0:
        print("y > 0")
    elif y % 1 != 0:
        print("y - дробное число")
    elif y < 0 and y % 1 == 0:
        return 1 / (x ** (-y))
        """ Второй вариант
        res = 1
        while y:
            res = res * 1 / x
            y += 1
        return res
        """
    return None


print("Возведение в степень: ", my_func(input("Введите x: "), input("Введите y: ")))

zagolovok("5")


def sum_str():
    cur_fun = True
    res = 0

    while cur_fun:
        my_list = input("Введите строку чисел через пробел: ")
        sum_str_split = my_list.split()
        promRes = 0
        for i in sum_str_split:
            if i == "q":
                cur_fun = False
            else:
                try:
                    promRes = promRes + float(i)
                except ValueError:
                    print("Неверно введённое число")
                    cur_fun = False

        res = res + promRes
        if cur_fun:
            print(str(promRes) + "(" + str(res) + ")")
        else:
            print(promRes)


sum_str()

zagolovok("6")


def int_func(my_str):
    my_str = my_str.lower()
    return my_str.title()


def int_fun_str(my_str):
    my_str = my_str.split()
    res = ""
    for i in my_str:
        res = res + " " + int_func(i)

    print(res)


print(int_func(input("Введите слово: ")))
int_fun_str(input("Введите строку: "))

