# Задачи:
# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
#     Примеры:
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет


# print('введите первое число')
# a = int(input())
# print('введите второе число')
# b = int(input())
# print("является квадратом")
# if(a**2 == b or b**2 == a):
#     print("является квадратом")
# else:
#     print("не является квадратом")
 


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90







# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N   
#     Примеры:   
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input("введите целое число "))
for number in range(-n, n+1):
    print(number, end=" ")




# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.    
#     Примеры:    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

print (int(float(input("введите число ")) * 10) % 10)



# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.



# Первая задача
a = int(input())
b = int(input())
if a**2 == b or b**2 == a:
    print("yes")
else:
    print("no")

# 2я
some_list = []
for i in 1, 2, 3, 4, 5:
    some_list.append(int(input()))
print(some_list)
max = some_list[0]
for i in some_list:
    if max < i:
        max = i
print(max)

# 3
n = int(input("N="))
for i in range(-n, n+1):
    print(i)

# 4
x = float(input())*10
x = int(x) % 10
print(x)

# 5
number = int(input("число - "))
if (number % 5 == 0 and number % 10 == 0 and number % 30 != 0) or (number % 15 == 0 and number % 30 != 0):
    print(True)
else:
    print(False)

# 5_1
number = int(input("число - "))


def someFunc(n):
    if (number % 5 == 0 and number % 10 == 0 and number % 30 != 0) or (number % 15 == 0 and number % 30 != 0):
        return True
    else:
        return False


print(someFunc(number))
