# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
def striptrepitDigitsList(digits):
    nonRepitDigits=[]
    for i in range(len(digits)):
        if digits.count(digits[i])==1:
            nonRepitDigits.append(digits[i])
    print(nonRepitDigits)
    return nonRepitDigits
def getRandomRepitValueList(length):
    if length<0:
        print('Отрицательное количество элементов!')
        return []
    digits = list(range(10))
    digits=random.choices(digits, k=length)
    print(digits)
    return digits

striptrepitDigitsList(getRandomRepitValueList(int(input('Размер списка:'))))