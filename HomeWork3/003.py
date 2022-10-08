#  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

def getRandomFracList(size):
    if size<0:
        size=-size
    result=[0.0]*size
    for i in range(size):
        result[i]=round(random.uniform(0,10),2)
    print(result)
    return result

def minMaxDiffValueInList(List):
    minf=List[0]-List[0]//1
    maxf=minf
    for i in range(len(List)):
        fract=List[i]-List[i]//1
        if fract>maxf:
            maxf=fract
        if fract<minf:
            minf=fract
    print('Min: ',round(minf,2),' Max: ',round(maxf,2),end=' ')
    return round(maxf-minf,2)

print('Difference: ',minMaxDiffValueInList(getRandomFracList(int(input('Размер списка:')))))

