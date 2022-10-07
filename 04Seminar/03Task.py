# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 2, 3, 3, 4, 2]
# Сперва множество используется для получения уникальных значений. После этого множество превращается в список.
unique_numbers = list(set(numbers))
print(unique_numbers)

numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
