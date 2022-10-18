# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

number = int(input("Введите целое число n: \n"))

def setArrList(num):
    arrList = [0] * num
    i = 1
    for i in range(1, num+1):
        arrList[i-1] = int(round((1 + 1/i) ** i, 0))
    return arrList

def calcSumElems(arrLi):
    sum = 0
    for i in range(len(arrLi)):
        sum += arrLi[i]
    return sum

arrNums = setArrList(number)

print(f"Для n = {number}: {arrNums} -> {calcSumElems(arrNums)}")
