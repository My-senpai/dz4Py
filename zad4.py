# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from random import seed
seed()
k = int(input('Введите k = '))
a = open('file1.txt', 'w')
list = []
b = '=0'
for i in range(k+1):
    list.append(randint(0,101))
    if list[i] != 0:
        if i == 0:
            b = '+' + str(list[i]) + b
        elif i == 1:
            b = '+' + str(list[i]) +'*x' + b
        elif i == k:
            b = str(list[i]) +'*x^' + str(i) + b
        else:
            b = '+' + str(list[i]) +'*x^' + str(i) + b
a.writelines(b)
a.close()