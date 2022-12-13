days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
with open("trains.txt", 'w', encoding = 'utf-8') as in_file:
    for day in days:
        in_file.write(f'{day}\n')
print('Рабочее место диспетчера станции "Терновка"')
temp_day = str(input('Какой сегодня день? '))
if temp_day in days:
    spisok = [str(i) for i in input('Какие поезда проехали сегодня? ').split(" ")]
    print(spisok)
else:
    print('Введите день правильно.')
    while temp_day not in days:
        temp_day = str(input('Какой сегодня день? '))
        spisok = [str(i) for i in input('Какие поезда проехали сегодня? ').split(" ")]

with open("trains.txt", 'r', encoding = 'utf-8') as in_file:
    for line in in_file.readlines():
        print(line, end= '')
        if temp_day == line:
            in_file.write(f'{line} : В этот день проехали {spisok}')