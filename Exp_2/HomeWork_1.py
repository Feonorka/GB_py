# Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
x = int(input('Введите число X:'))
y = int(input('Введите число Y:'))
count = 0

for i in range(y - x):
    if i == 0 and x % 2 == 0 and x % 3 == 0:
        count += 1
    if (x + i) % 2 == 0 and (x + i) % 3 == 0:
        count += 1
    
print(f'Количество чисел, удовлетворяющих условия: {count}')