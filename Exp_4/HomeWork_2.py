# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

import random
spisok = [[random.randint(-5, 5) for x in range(random.randint(1, 10))] for x in range(random.randint(1, 10))]
temp_sum = list()
avr_dict = dict()
for item in spisok:
    lst = tuple(item)
    sum_num = 0
    i = 1
    for i in lst:
        sum_num += i
        temp_sum.append(sum_num)
    avr_dict[i] = temp_sum
    i += 1
    
    print(item)
print()
print(temp_sum)
print()
print(avr_dict)