#Сделать игру морской бой
import random

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
        if fire_coord_alf not in alf or fire_coord_num not in nums or len(fire_list) > 2:    # Проверка правильности ввода координат
            while fire_coord_alf not in alf or fire_coord_num not in nums or len(fire_list) > 2:
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
    if queue_status == 'enemy':                                         # Ходы компьютера берутся рандомно
        fire_coord = random.choice(alf) + str(random.choice(nums))
        return fire_coord

def ship_place(ships_types, alf, nums):                               # Рандомно расставляет корабли
    battle_map = {}
    for types in ships_types:
        temp_list_of_val = ships_types.get(types)
        num_deck = temp_list_of_val[1]                                # Определяет количество палуб у корабля из его характеристик
        col_ships = temp_list_of_val[0]                               # Определяет количество кораблей определенного типа на поле
        temp_list_of_val[2] = [[str(random.choice(alf)) + str(random.randint(1, len(nums))) for y in range(col_ships)] for x in range(num_deck)]
       
        battle_map[types] = temp_list_of_val[2]
    return battle_map

def miss_or_not(fire_coord, battle_map):    # На вход принимает координату куда производится выстрел и словарь с координатами кораблей
    if fire_coord in battle_map:            # Возвращает нужный символ, в зависимости от того совпали координаты или нет
        print(f'Снаряд летит и попадает по кораблю на {fire_coord}')
        return fire_place
    else:
        print(f'Снаряд после попадания в {fire_coord} издал глухой булькающий звук...')
        return miss_place

def queue(fire_coord, pre_status, battle_map, player_go, enemy_go, num_go_p, num_go_e):  # Возвращает значения player\enemy в зависимости от того чья сейчас очередь
    queue_list = ['player', 'enemy']                                
                                                                    # На входе получает координату из функции fire() и данные о сделанных ходах из
                                                                    # отдельных словарей
    if fire_coord not in battle_map and pre_status == 'player':     # Переход хода в случа если игрок совершил промах
        queue_status = queue_list[1]
    elif fire_coord in battle_map and pre_status == 'player':
        queue_status = queue_list[0]
  
    if fire_coord not in battle_map and pre_status == 'enemy':    # Переход хода в случа если компьютер совершил промах
        queue_status = queue_list[0]
    elif fire_coord in battle_map and pre_status == 'enemy':
        queue_status = queue_list[1]
    
    if pre_status == queue_list[0]:                               # Запись ходов в индивидуальный словарь ходов, чтобы знать куда не стрелять
        player_go[num_go_p] = str(fire_coord)
    else:
        enemy_go[num_go_e] = str(fire_coord)
                       
    return queue_status

def alr_shoot(fire_coord, pre_status, player_go, enemy_go):                             # Проверяет не делался ли выстрел ранее
    if pre_status == 'player'and fire_coord in player_go.values():
        return False
    elif pre_status == 'enemy'and fire_coord in enemy_go.values():
        return False
    else:
        return True
    

ships = {'Линкор': [1, 4, []], 'Крейсер': [2, 3, []], 'Эсминец': [3, 2, []], 'Катер': [4, 1, []]}   # В словаре, в качестве значений, указаны:
alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']                                            # количество кораблей определенного типа, количество палуб и словарь хранящий координаты
nums = [x for x in range(1,11)]
player_go = {}                                                                                      # В словарях записываются ходы
enemy_go = {}
empty_place = ' .'
fire_place = '#'
miss_place = '*'
ship_on_field = 'Ж'
num_go_p = 1
num_go_e = 1

print('Игра начинается...')
print('Корабли противника размещены...')
enemy_map = ship_place(ships, alf, nums)
enemy_list = []
for ship in enemy_map:
    for ds in enemy_map[ship]:
        for lm in ds:
            enemy_list.append(lm)
print(enemy_list)
print('Ваши корабли тоже...')
player_map = ship_place(ships, alf, nums)
player_list = []
for ship in player_map:
    for ds in player_map[ship]:
        for lm in ds:
            player_list.append(lm)
print(player_list)
print()
pre_status = 'player'
print('Это 1 по счету ход')
print(f'Сейчас ходит: {pre_status}')
first_shot = fire(pre_status)
miss_or_not(first_shot, enemy_list)
pre_status = queue(first_shot, pre_status, enemy_list, player_go, enemy_go, num_go_p, num_go_e)
num_go_p += 1
print(f'Следующий ход за: {pre_status}')
print()

for i in range(2, 16):
    print(f'Это {i} по счету ход')
    shot = fire(pre_status)
    while alr_shoot(shot, pre_status, player_go, enemy_go) == False:
        shot = fire(pre_status)
    print('----------------------------')
    if pre_status == 'player':  
        print(f'Сейчас ходит: {pre_status}')
        print(f'Произведен выстрел по {shot} на поле enemy')
        player_que = queue(shot, pre_status, enemy_list, player_go, enemy_go, num_go_p, num_go_e)
        miss_or_not(shot, enemy_list)
        enemy_list = list(filter((shot).__ne__,enemy_list))
        print(f'Следующий ход за: {player_que}')
        pre_status = player_que
        num_go_p += 1
        print()
    else:
        print(f'Сейчас ходит: {pre_status}')
        print(f'Произведен выстрел по {shot} на поле player')
        enemy_que = queue(shot, pre_status, player_list, player_go, enemy_go, num_go_p, num_go_e)
        miss_or_not(shot, player_list)
        player_list = list(filter((shot).__ne__,player_list))
        print(f'Следующий ход за: {enemy_que}')
        pre_status = enemy_que
        num_go_e += 1
        print()
    print('----------------------------')
    print(f'Ваши ходы: {player_go}')
    print(f'Ходы Вашего соперника: {enemy_go}')
    print()