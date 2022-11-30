# Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
spisok = [int(i) for i in input('Введите значения: ').split()]
list_m = sorted(spisok)
max_num = 0
pre_max = 0

for lst in list_m:
    if max_num < lst:
        max_num = lst
    if lst >= pre_max and lst < max_num:
        pre_max = lst
print(f'Максимальное значение: {max_num}')
print(f'Второе максимальное значение: {pre_max}')