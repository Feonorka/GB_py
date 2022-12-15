#Сделать игру морской бой
import random
import collections

def field(queue_role):                                             # Вывод поля боя с координатами в терминал
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

def ship_place(ships_types, alf, nums):
    battle_map = {}
    for types in ships_types:
        temp_list_of_key = types
        temp_list_of_val = ships_types.get(types)
        num_deck = temp_list_of_val[1]                                # Определяет количество палуб у корабля из его характеристик
        col_ships = temp_list_of_val[0]                               # Определяет количество кораблей определенного типа на поле
        temp_list_of_val[2] = [[str(random.choice(alf)) + str(random.randint(1, len(nums))) for y in range(col_ships)] for x in range(num_deck)]
       
        battle_map[types] = temp_list_of_val[2]
        
        #print(f'Корабль типа: {temp_list_of_key} имеет {num_deck} палубы, всего в игре таких кораблей: {col_ships}')
        #print(battle_map)
        
    return battle_map

def miss_or_not(fire_coord, battle_map):  # На вход принимает координату куда производится выстрел и словарь с координатами кораблей
    if fire_coord in battle_map.values(): # Возвращает нужный символ, в зависимости от того совпали координаты или нет
        return fire_place
    else:
        return miss_place

def queue(fire_coord, battle_map, player_go, enemy_go):  # Возвращает значения player\enemy в зависимости от того чья сейчас очередь
    queue_list = ['player', 'enemy']                     # В словарях записываются ходы
    num_go_p = 1                                         # На входе получает координату из функции fire() и данные о сделанных ходах из
    num_go_e = 1                                         # отдельных словарей

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

ships = {'Линкор': [1, 4, []], 'Крейсер': [2, 3, []], 'Эсминец': [3, 2, []], 'Катер': [4, 1, []]}   # В словаре в качестве значений указаны значения
alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']                                            # количество кораблей определенного типа
player_go = {}
enemy_go = {}
nums = [x for x in range(1,11)]
empty_place = ' .'
fire_place = '#'
miss_place = '*'
ship_on_field = 'Ж'

print('Игра начинается...')
print('Корабли противника размещены...')
enemy_map =  ship_place(ships, alf, nums)
print('Ваши корабли тоже...')
player_map =  ship_place(ships, alf, nums)
while count_go != 100:
    queue_role = queue()
    field(queue_role)
    print(f'Сейчас ходит {queue()}')
    fire('player')
    count_go =  len(ships) + 