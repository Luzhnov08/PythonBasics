# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

number = int(input('Введите целое число N: \n'))

def calc_factr(num):
    if num == 1: return 1
    return num * calc_factr(num-1)

def printArr(num):
    numList = [0] * num
    for i in range(num):
        numList[i] = calc_factr(i+1)
    print(numList)

printArr(number)
