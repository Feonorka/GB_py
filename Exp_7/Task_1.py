from os import system
import datetime
import time
import datetime
print(datetime.datetime.today())
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
with open("trains.txt", 'w', encoding = 'utf-8') as in_file:
    for day in days:
        in_file.write(f'{day}\n')
now = datetime.datetime.now()

menu_options = {
    1: 'Ввести данные',
    2: 'Показать прошедшие за неделю',
    3: 'Прошедшие за сегодня',
    4: 'Exit'}
for i in range(10,0,-1):
    print(f"{i}", end="\r", flush=True)
    time.sleep(1)

def print_menu():
    print(now.strftime("%d-%m-%Y %H:%M"))
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def option1():
    print('Рабочее место диспетчера станции "Терновка"')
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
    temp_day = str(input('За какой день сделать запись? '))
    if temp_day in days:
        spisok = [str(i) for i in input('Какие поезда проехали сегодня? ').split(" ")]
        print(f'Добавить следующие записи: {spisok} в график за {temp_day }')
        
        if input('Введите "Y" для подтверждения: ') == 'Y':
            print('Запись добавлена')
            time.sleep(5)
        else:
            print('Изменения не сохранены')
            time.sleep(5)
    else:
        print('Введите день правильно.')
        while temp_day not in days:
            temp_day = str(input('Какой сегодня день? '))
            spisok = [str(i) for i in input('Какие поезда проехали сегодня? ').split(" ")]
            time.sleep(10)
    
def option2():
    in_file = open('trains.txt','r', encoding = 'utf-8')
    temp_list = in_file.readlines()
    for i in temp_list:
        print(i, end="")
    time.sleep(10)
    
def option3():
    print('Выбрана опция №3')
    time.sleep(10)
    

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Что Вы хотите сделать? '))
        except:
            print('Неправильный ввод...')
        if option == 1:
           option1()
           system('cls')
        elif option == 2:
            option2()
            system('cls')
        elif option == 3:
            option3()
            system('cls')
        elif option == 4:
            print('Спасибо что воспользовались терминалом!')
            system('cls')
            exit()
        else:
            print('Неверный вариант. Введите число от 1 до 4')