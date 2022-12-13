#Сделать игру морской бой
import random
import collections
ships = {'Линкор': [1, 4, []], 'Крейсер': [2, 3, []], 'Эсминец': [3, 2, []], 'Катер': [4, 1, []]}

alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
nums = [x for x in range(1,11)]
empty_place = ' .'
fire_place = '#'
miss_place = '*'
ship_on_field = 'Ж'

def field():                                             # Вывод поля боя с координатами в терминал
    for k in range(11):
        if k == 0: print(' '.center(1),"", end=" ")
        else:
            print(f'{k}'.center(1),"", end=" ")
    print()
    for i in alf:
        print(f'{i}'.center(1), "", end="")
        for j in range(10):
            print(f'{empty_place}'.rjust(2), end=" ")
        print()

def fire(queue_status):                     # На входе принимает статус - результат работы функции queue()
    if queue_status == 'player':            # В результате выдает координаты для выстрела
        temp_coord = str(input('Введите координату (в формате А1): '))
        fire_list = list(temp_coord)
        fire_coord_alf = str(fire_list[0])
        fire_coord_num = int(fire_list[1])
        if fire_coord_alf not in alf or fire_coord_num not in nums:    # Проверка правильности ввода координат
            while fire_coord_alf not in alf or fire_coord_num not in nums:
                print('Неправильный формат координат. Повторите')
                temp_coord = str(input('Введите координату (в формате А1)'))
                fire_list = list(temp_coord)
                fire_coord_alf = str(fire_list[0])
                fire_coord_num = int(fire_list[1])
                if fire_coord_alf in alf or fire_coord_num in nums:     # Запрос на ввод будет продолжаться до тех пор пока пользователь не введет
                    fire_coord = temp_coord                             # правильные данные
                    return fire_coord
        else:
            fire_coord = temp_coord
            return fire_coord
    if queue_status == 'enemy':
        fire_coord = random.choice(alf) + str(random.choice(nums))
        return fire_coord

def ship_place():
    count_ship = 0
    while count_ship < len(ships):
        for deck in ships:
            temp_list = ships.get(deck)
            ships_deck = {deck:{'Количество' : temp_list[0],'Жизни' : temp_list[1], 'Координаты': temp_list[2]}}
            print(ships_deck)
            count_ship += 1
    return battle_map

def miss_or_not(fire_coord, battle_map):  # На вход принимает координату куда производится выстрел и словарь с координатами кораблей
    if fire_coord in battle_map.values(): # Возвращает нужный символ, в зависимости от того совпали координаты или нет
        return fire_place
    else:
        return miss_place

def queue(fire_coord, battle_map):  # Возвращает значения player\enemy в зависимости от того чья сейчас очередь
    player_go = {}                  # В словарях записываются ходы
    enemy_go = {}                   # На входе получает координату из функции fire()
    queue_list = ['player', 'enemy']
    num_go_p = 1
    num_go_e = 1

    if len(player_go) == 0 and len(enemy_go) == 0:  # Условие для определения первого хода (по умолчанию первым ходит игрок)
        queue_status = queue_list[0]                # При первом ходе другие условия не проверяются
        player_go[num_go_p] = fire_coord
        num_go_p += 1
        return queue_status
        
    else:
        if fire_coord not in battle_map and queue_status == 'player':   # Переход хода в случа если игрок совершил промах
            queue_status = queue_list[1]
        else: queue_status = queue_list[0]

    if fire_coord not in battle_map and queue_status == 'enemy':        # Переход хода в случа если компьютер совершил промах
        queue_status = queue_list[0]
    else: queue_status = queue_list[1]

    if queue_status == queue_list[0]:                                   # Запись ходов в индивидуальный словарь ходов, чтобы знать куда не стрелять
        player_go[num_go_p] = fire_coord
        num_go_p += 1

    else:
        queue_status == queue_list[1]
        enemy_go[num_go_e] = fire_coord
        num_go_e += 1
               
    return queue_status

print()
print('Игра начинается...')
print()
ship_place()
print('Корабли противника размещены...')
print()
print('Разместите Ваши корабли...')
print()
ship_place()

battle_map = ship_place()

field()
print()

scuter_fire = fire('player')
miss_or_not(scuter_fire, battle_map)
queue(scuter_fire, battle_map)

print(f'Правила:\nУ каждого игрока в начале игры {len(ships)} вида кораблей.\n')
