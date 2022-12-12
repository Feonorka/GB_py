#Сделать игру морской бой
import random
import collections
ships = {'Линкор': [1, 4, []], 'Крейсер': [2, 3, []], 'Эсминец': [3, 2, []], 'Катер': [4, 1, []]}

alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
nums = [x for x in range(1,11)]
empty_place = ' .'
fire_place = '#'
miss_place = '*'

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

def fire(queue_status):
    if queue_status == 'player':
        fire_coord = str(input())
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
    return #battle_map

def miss_or_not(fire_coord, battle_map):  # На вход принимает координату куда производится выстрел и словарь с координатами кораблей
    if fire_coord in battle_map.values(): # Возвращает нужный символ, в зависимости от того совпали координаты или нет
        return fire_place
    else:
        return miss_place   

def queue(fire_coord, battle_map):  # Возвращает значения player\enemy в зависимости от того чья сейчас очередь
    player_go = {}                  # В словарях записываются ходы
    enemy_go = {}                   # На входе получает координату из функции fire()
    queue_list = ['player', 'enemy']
    num_go = 1

    if len(player_go) == 0 and len(enemy_go) == 0:
        queue_status = queue_list[0]
    else:
        if fire_coord not in battle_map:
            queue_status = queue_list[0]


    if queue_status == queue_list[0]:
        player_go[num_go] = fire_coord
    else:
        queue_status == queue_list[1]
        enemy_go[num_go] = fire_coord
               
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
start_queue_status = 'player'
battle_map = ship_place()
queue(start_queue_status, battle_map)
field()
print()
print(f'Правила:\nУ каждого игрока в начале игры {len(ships)} вида кораблей.\n')
