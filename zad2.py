# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('введите натуральное число '))

lst = []
d = 2
while d <= n:
    if n%d == 0:
        lst.append(d)
        n = n/d
    else:
        d += 1
print('простые множители числа', lst)