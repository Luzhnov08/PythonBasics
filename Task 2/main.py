# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def CheckFormula(x, y, z):
    leftSide = not(x or y or z)
    rightSide = not (x) and not (y) and not (z)
    return leftSide == rightSide

def PrintResult(chck):
    if chck == 1:
        print("Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно")
    else:
        print("Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно")

cX = int(input("Введите значение (целое число) координаты X: "))
cY = int(input("Введите значение (целое число) координаты Y: "))
cZ = int(input("Введите значение (целое число) координаты Z: "))
bool check = CheckFormula(cX, cY, cZ)
PrintResult(check)