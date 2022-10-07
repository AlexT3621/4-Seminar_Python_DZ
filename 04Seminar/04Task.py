# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0
import random
k = 5
x = 'x'
fileW = open('text05.txt', 'w')
for i in range(k+1):
    b = random.randint(0, 101)
    if k > 0:
        elem = f'{b}x^{k}+'
        k = k-1
        # list.append(elem)
        fileW.write(elem)
    else:
        elem = f'{b}=0'
        fileW.write(elem)


fileW.close()
print(list)
f = open('text05.txt', 'r')
l = [line.strip() for line in f]
f.close()

print(l)
