# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

import random
spisok = [[random.randint(0, 5) for x in range(random.randint(1, 5))] for x in range(random.randint(1, 5))]
print(spisok)
print()

avr_dict = dict()
count = 0
for item in spisok:
    lst = tuple(item)
    sum_num = 0
    
    for i in lst:
        sum_num += i
        #temp_sum.append(sum_num)
    avr_dict[count] = round((sum_num / len(lst)), 2)
    count += 1
print()
print(avr_dict)