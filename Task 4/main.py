import math

# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
#- 3
#- 6
#- 2
#- 1

# out
#5.099


def PrintLenBetweenPoints(Ax, Ay, Bx, By):
    result = math.sqrt(math.pow(Bx - Ax, 2) + math.pow(By - Ay, 2))
    print("Расстояние между точками равно: ")
    print(result.__round__(3))

pointAx = int(input("Введите координату X для первой точки: "))
pointAy = int(input("Введите координату Y для первой точки: "))
pointBx = int(input("Введите координату X для второй точки: "))
pointBy = int(input("Введите координату Y для второй точки: "))

PrintLenBetweenPoints(pointAx, pointAy, pointBx, pointBy)