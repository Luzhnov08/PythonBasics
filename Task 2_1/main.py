# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = float(input('Введите вещественное число: '))

n = len(str(number)) -1
number = int(number * 10 ** n)

res = 0
for i in range(n*2):
    number = number // 10
    res += number % 10

print('Сумма цифр введенного числа: ' + str(res))