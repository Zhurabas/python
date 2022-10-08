# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


from random import sample

def getRandomList(size):
    if size<0:
        size=-size
    result=sample(range(10),size)
    print(result)
    return result

def oddElemListSum(list):
    sum=0
    for i in range(len(list)):
        if i%2==0:
            sum+=list[i]
    return sum


print(oddElemListSum(getRandomList(int(input('Введите размер списка: ')))))
