# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input('Введите число '))
list = []
mnozh = 2
while num > 1:
    if num % mnozh == 0:
        list.append(mnozh)
        num = num/mnozh
    else:
        mnozh += 1
print(list)
