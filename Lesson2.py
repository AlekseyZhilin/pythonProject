print("-" * 20 + "Задание1" + "-" * 20)
list1 = ["Python", 3.8, True, None, [1, 2, 3]]
for el in range(len(list1)):
    print("Элемент " + str(el) + ":" + str(list1[el]) + " тип - " + str(type(list1[el])))

# -------------------------------------
print("-" * 20 + "Задание2" + "-" * 20)
list2 = []
print("Для завершения ввода списка напишите 'end'")
while True:
    el = input("Введите " + str(len(list2) + 1) + " элемент списка: ")
    if el == "end":
        break
    list2.append(el)

print("Значения введённого списка до перестанвок", list2)
for i in range(len(list2)):
    if i % 2 != 0 and i >= 1:
        temp = list2[i - 1]
        list2[i - 1] = list2[i]
        list2[i] = temp

if len(list2) >= 2:
    print("Значения введённого списка после перестанвок", list2)
else:
    print("Перестановок не было т.к. список состоит из менее чем 2 элементов")

# -------------------------------------
print("-" * 20 + "Задание3" + "-" * 20)
list3 = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
dict1 = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
         9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
num = int(input("Введите номер месяца: "))
if (num >= 0) and (num <= 12):
    print("Время года - " + str(list3[num - 1]) + " (через список)")
    print("Время года - " + str(dict1.get(num)) + " (через словарь)")
else:
    print("Неверно введёный номер месяца")

# -------------------------------------
print("-" * 20 + "Задание4" + "-" * 20)
str1 = input("Введите строку: ")
list4 = str1.split()
for i, el in enumerate(list4):
    if len(el) <= 10:
        print(str(i) + ": " + el)
    else:
        print(str(i) + ": " + el[:10])

# -------------------------------------
print("-" * 20 + "Задание5" + "-" * 20)
list5 = [7, 5, 3, 3, 2]
print("Для завершения ввода списка напишите 'end'")
while True:
    el = input("Введите элемент рейтинга: ")
    if el == "end":
        break
    el = int(el)

    if list5.count(el):
        ind = list5.index(el) + list5.count(el)
        list5.insert(ind, el)
    else:
        for i, cur_i in enumerate(list5):
            if el > cur_i:
                list5.insert(i, el)
                break
        if list5[len(list5) - 1] > el:
            list5.append(el)
    print("Рейтинг после подстановки элемента: ", list5)

# -------------------------------------
print("-" * 20 + "Задание6" + "-" * 20)
list6 = []
ind = 0
while True:
    name = input("Введите наименование товара: ")
    if name == "end":
        break
    price = float(input("Введите цену товара: "))
    col = int(input("Введите количество товара: "))
    izm = input("Введите единицу измерения: ")
    ind += 1
    list6.append((ind, {"название": name, "цена": price, "количество": col, "ед": izm}))

my_list = [[], [], [], []]
for el in list6:
    i = 0
    for val in el[1].values():
        if not my_list[i].count(val):
            my_list[i].append(val)
        i += 1

print("Название: ", my_list[0])
print("Цена: ", my_list[1])
print("Количество: ", my_list[2])
print("Ед: ", my_list[3])
