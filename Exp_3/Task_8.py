#3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
my_str = str(input('Введите строку: '))
search = 'в'
while my_str.count(search) < 2:
    my_str = str(input('Введите строку: '))
my_str.lower
start = 0
end = len(my_str)
count = 0
for i in range(len(my_str)):
    if search in my_str[start::]:
        ipos = my_str.index(search, start, end)
        start = ipos + 1
    if count == 2:
        break
print(f'Индекс искомого символа: {ipos}')
