# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def printDecToBin(dec):
    if dec==0:
        print(dec)
        return
    elif dec!=1:
        printDecToBin(dec//2)
    print(dec%2, end='')
    

printDecToBin(88)
print()
printDecToBin(11)
