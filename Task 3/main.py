# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def PrintQuarter(x, y):
    if (x > 0 and y > 0):
        resText = "1 четверть"
    elif (x < 0 and y > 0):
        resText = "2 четверть"
    elif (x < 0 and y < 0):
        resText = "3 четверть"
    elif (x > 0 and y < 0):
        resText = "4 четверть"
    else:
        resText = "Введены некорретные координаты"
    print(resText)

posX = int(input("Введите координату X: "))
posY = int(input("Введите координату Y: "))
PrintQuarter(posX, posY)