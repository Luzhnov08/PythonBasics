# * 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов,# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

number1 = int(input("Введите первое целое число: \n"))
number2 = int(input("Введите второе целое число: \n"))
countItems = int(input("Введите целое число количества элементов: \n"))

def setArrList(cntItms):
    cntItms = cntItms * 2 + 1
    arrList = [0] * cntItms
    arrList[0] = int((cntItms - 1) / 2 * -1)

    for i in range(1, cntItms):
        arrList[i] = arrList[i-1] + 1
    return arrList

def multByPos(posOne, posTwo, arrElems):
    mult = (arrElems[posOne-1] * arrElems[posTwo-1])
    print(f"-> {mult}")

arrNums = setArrList(countItems)
print(f"-> {arrNums}")
multByPos(number1, number2, arrNums)