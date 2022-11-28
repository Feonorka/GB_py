#3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего

my_str = str(input('Введите строку: '))
on_str = ''
on_ind = 0
max_ind = 0
i = 0

for i in range(len(my_str)):
    on_ind = my_str.count(my_str[i])
    if on_ind > max_ind:
        max_ind = on_ind
        on_str = my_str[i]
print(f'Элемент {on_str} встречается наибольшее количестов раз, а именно: {max_ind}')