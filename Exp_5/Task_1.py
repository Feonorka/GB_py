import random
game_var = ['Камень', 'Ножницы', 'Бумага']

end_score = int(input('Введите число выигранных туров для победы: \n'))
score_dict = {'player' : 0, 'comp': 0}

games_dict = {'player', 'comp'}
print(games_dict)

player_game_chose = str(input('Сделайте выбор: '))
print(f'Пользователь выбрал: {player_game_chose}\n')
comp_game_chose = random.choice(game_var)
print(f'Компьютер выбрал: {comp_game_chose}\n')

if score_dict['player'] == end_score:
    print(f'Выиграл игрок')
if score_dict['comp'] == end_score:
    print(f'Выиграл компьютер')

print(bool(game_var[0]))
print(bool(game_var[1]))
print(bool(game_var[2]))
