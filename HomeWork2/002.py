#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#- 4 -> [1, 2, 6, 24]
#- 6 -> [1, 2, 6, 24, 120, 720]
result=1
n=int(input('Введите число: '))
for i in range(n):
    result*=i+1
    print(result)