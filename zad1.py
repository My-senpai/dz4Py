# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
d = float(input("при d = "))
count = 0
while d < 1:
    d = d*10
    count += 1
a = math.pi
print((str(a)[:count+2]))