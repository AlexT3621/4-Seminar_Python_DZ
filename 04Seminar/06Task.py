# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
f = open('text6_1.txt', 'r')
l = [line.strip() for line in f]
f.close()
f1 = open('text6_2.txt', 'r')
l1 = [line.strip() for line in f1]
f1.close()

print(l)
print(l1)
