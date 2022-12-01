# Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
spisok = [int(i) for i in input().split()]
max_item = 0
pre_max = 0
max_id = 0
for item in spisok:
    if item > max_item:
        max_item = item
        max_id = spisok.index(item)
for item in spisok:    
    if item > pre_max and spisok.index(item) != max_id:
        pre_max = item
print(f"Максимальный элемент: {max_item}")
print(f"Предмаксимальный элемент: {pre_max}")