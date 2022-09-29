# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# - 1 x > 0, y > 0
# - 3 x < 0, y < 0
# - 33 "Введена некорретная четверть!"

def PrintCoordinates(quart):
    if (quart==1):
        resText = "x > 0, y > 0"
    elif (quart==2):
        resText = "x < 0, y > 0"
    elif (quart==3):
        resText = "x < 0, y < 0"
    elif (quart==4):
        resText = "x > 0, y < 0"
    else:
        resText = "Введена некорретная четверть!"
    print(resText)

quarter = int(input("Введите номер четверти от 1 до 4: "))
PrintCoordinates(quarter)