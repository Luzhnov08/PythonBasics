# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import random, randint

number = int(input("Введите целое число: "))

def setValuesInArr(num):
    itemsArr = [0] * num

    for i in range(num):
        itemsArr[i] = int(i)

    printArr(itemsArr)
    return itemsArr

def shakeItArr(arrNums):
    buff = 0
    rndPos = 0

    for n in range(len(arrNums)):
        buff = arrNums[n]
        rndPos = randint(1, 9)
        arrNums[n] = arrNums[rndPos]
        arrNums[rndPos] = buff

        for m in range(len(arrNums)):
            buff = arrNums[m]
            rndPos = randint(1, 9)
            arrNums[m] = arrNums[rndPos]
            arrNums[rndPos] = buff

    printArr(arrNums)

def printArr(arrNums):
    print(f'-> {arrNums}')

arrNumbers = setValuesInArr(number)
shakeItArr(arrNumbers)