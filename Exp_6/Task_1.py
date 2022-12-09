#Правильной скобочной последовательностью называется строка, состоящая только из символов «скобки»
# (открывающих "(" и закрывающих ")"), где каждой закрывающей скобке найдётся соответствующая открывающая.
# Например, () и (()()) — правильные последовательности, а (()(() или )( — нет.
#Напишите функцию , которая проверяет, является ли поступившая на вход строка правильной скобочной последовательностью.
# Если да, она должна печатать YES, в противном случае — NO.
# Обратите внимание, что пустая строка также является правильной скобочной последовательностью.
str_in = str(input('Введите строку: '))

#def right_sec(str_input):
    
#str_list = list(str_input)
str_list = list(str_in)
open_r = str_list.count('(')
close_r = str_list.count(')')
if open_r != close_r:
    print('NO')
elif str_list.index('(') > str_list.index(')'):
    print('NO')
elif ('(' in str_list and ')' not in str_list) or (')' in str_list and '(' not in str_list):
    print('NO')
        #return 'NO'
else:
    for item in str_in:
        temp_r = int(str_list.index('('))

        #return 'YES'
print(temp_r)
#print(right_sec(str_in))