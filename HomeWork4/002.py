# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def getNaturalDigitsList(digit):
    counter=2
    naturalDigits=[]
    while digit!=1:
        if not digit%counter:
            naturalDigits.append(counter)
            digit/=counter
            counter=2#если минимальный простой множитель найден - сброс множителя
        else:
            counter+=1#иначе ищем дальше
    return naturalDigits


print('Cписок простых множителей числа:',getNaturalDigitsList(int(input('Задайте натуральное число:'))))