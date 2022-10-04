#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import sample
def pairSumInList(List):
    sum=[0]
    for i in range(len(List)//2):
        sum.append(List[i]*List[len(List)-i-1])
    if not len(List)%2==0:#У среднего элемента нет пары, по логике это и не нужно, но в примере он пишется, поэтому есть эта проверка.
        sum.append(List[len(List)-len(List)//2-1])
    sum.remove(0)
    return sum

digits=list(sample(range(10),10))
print(digits)
print(pairSumInList(digits))