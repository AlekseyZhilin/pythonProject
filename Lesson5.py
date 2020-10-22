import json
print("-" * 20 + "Задание1" + "-" * 20)

try:
    file = open("text1.txt", "w", encoding="utf-8")
    while True:
        write_str = input("Введит строку в файл (пустая строка - окончание ввода): ")
        if write_str == "":
            file.close()
            break
        file.write(write_str + "\n", )
except IOError:
    print("Ошибка записи файла")

print("-" * 20 + "Задание2" + "-" * 20)
try:
    file = open("text2.txt", "r", encoding="utf-8")
    content = file.readlines()
    col_slov_obsh = 0
    for str_i in range(len(content)):
        cur_str = content[str_i].split()
        col_slov = [i for i in range(len(cur_str))][-1] + 1
        col_slov_obsh += col_slov
        print(f"{str_i + 1} строка, количество слов - {col_slov}")
    file.close()
    print(f"Общее количество строк: {str_i + 1} Общее количество слов: {col_slov_obsh}")
except IOError:
    print("Ошибка записи файла")

print("-" * 20 + "Задание3" + "-" * 20)
list_st = []
with open("text3.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
try:
    for el in content:
        cur_str = el.split()
        if len(cur_str) < 2:
            continue
        if float(cur_str[1]) < 20000:
            list_st.append([cur_str[0], float(cur_str[1])])
except ValueError:
    print("Неверно введённый оклад в файле")

zar = 0
for i in list_st:
    zar += i[1]
    print(f"{i[0]:<15}{i[1]}")

print(f"Средняя зарплата {round(zar / (len(list_st)), 2)}")

print("-" * 20 + "Задание4" + "-" * 20)
new_dict = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
new_list = []
with open("text4.txt", "r", encoding="utf-8") as file:
    for line in file:
        for key, val in new_dict.items():
            if line.count(key):
                new_list.append(line.replace(key, val))

with open("text4_1.txt", "w", encoding="utf-8") as file:
    file.writelines(new_list)

print("-" * 20 + "Задание5" + "-" * 20)

new_list = [str(i) for i in range(1, 9)]
new_list = " ".join(new_list)
try:
    with open("text5.txt", "w+", encoding="utf-8") as file:
        file.writelines(new_list)
        file.seek(0)
        content = file.readlines()
    content = content[0].split()
    content = map(float, content)
    print("Сумма чисел файла = ", sum(content))
except IOError:
    print("Ошибка чтения записи файла")
except ValueError:
    print("Ошибка конвертации типов данных")

print("-" * 20 + "Задание6" + "-" * 20)
my_dict = {}
try:
    with open("text6.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    for el in content:
        cur_str = el.split()
        my_dict.update({f"{cur_str[0]}": [i for i in cur_str[1:] if i != "—"]})
except IOError:
    print("Ошибка чтения файла")
except ValueError:
    print("Ошибка конвертации типов данных")

my_list = [0, 0, 0]
try:
    for key, val in my_dict.items():
        print(f"{key:<15}", ", ".join(val))
        for i in val:
            if i.find("(л)") != -1:
                my_list[0] += float(i[0:i.find("(л)")])
            elif i.find("(пр)") != -1:
                my_list[1] += float(i[0:i.find("(пр)")])
            elif i.find("(лаб)") != -1:
                my_list[2] += float(i[0:i.find("(лаб)")])
except ValueError:
    print("Ошибка обработки данных")
else:
    print(f"Количество часов лекций: {my_list[0]}, практик: {my_list[1]}, лабораторных работ: {my_list[2]}")

print("-" * 20 + "Задание7" + "-" * 20)
my_list = []
try:
    with open("text7.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    for el in content:
        cur_str = el.split()
        my_list.append({f"{cur_str[0]}": float(cur_str[2]) - float(cur_str[3])})
except IOError:
    print("Ошибка чтения файла")
except ValueError:
    print("Ошибка конвертации типов данных")

average_profit = 0
col = 0
try:
    for el in my_list:
        print(el)
        val = [i for i in el.values()]
        if val[0] > 0:
            average_profit += val[0]
            col += 1

    average_profit /= col
    print("Средняя прибыль = ", average_profit)
except ValueError:
    print("Ошибка обработки данных")
else:
    my_list.append({"average_profit": round(average_profit, 2)})
    with open("text_json.json", "w") as file:
        json.dump(my_list, file)

