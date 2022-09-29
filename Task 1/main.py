# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def PrintDay(dayNumber):
    if (dayNumber == 6 or dayNumber == 7):
        resText = "Да, выходной"
    elif (dayNumber in range(1, 6)):
        resText = "Нет, не выходной, всё хорошо"
    else:
        resText = "Было введено некорректное число"
    print(resText)

dayNumber = int(input("Введите целое число от 1 до 7:"))
PrintDay(dayNumber)
