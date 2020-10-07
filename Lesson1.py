print("Задание 1")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

name = input("Введите ваше имя: ")
age = int(input("Сколько вам лет: "))
facultet = input("На каком факультете вы обучаетесь: ")

print(f"Здравствуйте, {name}, Ваш возраст: {age}, факультет обучения: {facultet}")

print("Задание 2")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

sec = minute = chas = 0
timeSec = int(input("Введите время в секундах: "))
if timeSec < 60:
    sec = timeSec
elif (timeSec >= 60) and (timeSec < 60 * 60):
    minute = timeSec // 60
    sec = timeSec % 60
else:
    chas = timeSec // (60 * 60)
    minute = (timeSec % (60 * 60)) // 60
    sec = (timeSec % (60 * 60)) % 60

print(f"время в формате 'чч:мм:сс' {chas:02d}:{minute:02d}:{sec:02d}")

print("Задание 3")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

n = int(input("Введите число: "))
n2 = int(str(n) + str(n))
n3 = int(str(n) + str(n) + str(n))

print("Сумма чисел n + nn + nnn = ", n + n2 + n3)

print("Задание 4")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

val = int(input("Введите целое положительное число: "))
enterVal = val
maxVal = 0
curVal = 0
while val // 10:
    curVal = val % 10
    val = val // 10
    if maxVal < curVal:
        maxVal = curVal
if maxVal < val:
    maxVal = val

print("Максимальная цифра в числе {} = {}".format(enterVal, maxVal))

print("Задание 5")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

viruchka = float(input("Введите значение выручки фирмы: "))
isderzki = float(input("Введите издержки фирмы: "))
finResult = viruchka - isderzki
if finResult > 0:
    print(f"Фирма работает с прибылью: {finResult:.2f}")
    print("Рентабельность: ", finResult / viruchka)
    colSotr = int(input("Введите численность сотрудников: "))
    print("Прибыль в расчёте на одного сотрудника:", finResult / colSotr)
if finResult < 0:
    print(f"Фирма работает с убытками {finResult:.2f}")

print("Задание 6")
strLes = "-"
count = 0
while count < 50:
    strLes += "-"
    count += 1
print(strLes)

curResult = float(input("Введите результат спортсмена в первый день: "))
resKilometr = float(input("Введите требуемый результат в километрах: "))
resDay = 0
while curResult <= resKilometr:
    resDay += 1
    print(f"{resDay}-й день: {curResult}")
    curResult = curResult + curResult * 0.1
resDay += 1
print(f"{resDay}-й день: {curResult}")
curResult = curResult + curResult * 0.1
print(f"Ответ: на {resDay}-й день спортсмен достиг результата не менее {resKilometr} км")
