# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
b = int(input('vvedi '))
a = [random.randint(0, 10) for i in range(b)]
print(a)

c = []
for i in a:
    if a.count(i) == 1:
        c.append(i)
print(c)