def find_items_backpack(items, max_weight):
    backpack = []
    total_weight = 0

    for item, weight in items.items():
        if total_weight + weight <= max_weight:
            backpack.append(item)
            total_weight += weight

    return backpack

# Пример использования
items = {
    'Треккинговые палки': 2,
    'Палатка': 3,
    'Спальный мешок': 2,
    'Котелок': 1,
    'Посуда': 1,
    'Фонарик': 1
}
max_weight = 7

result = find_items_backpack(items, max_weight)
print(result)

def find_shared_items(friends):
    # Находим вещи, которые есть у всех друзей
    common_items = set.intersection(*friends.values())
    
    # Находим вещи, которые есть только у одного друга
    unique_items = set.union(*friends.values()) - common_items
    
    # Находим вещи, которые есть у всех друзей кроме одного
    other_items = {}
    for friend, items in friends.items():
        other_friends_items = set.union(*(friends[f] for f in friends if f != friend))
        other_items[friend] = other_friends_items - items
    
    return common_items, unique_items, other_items

# Пример использования
friends = {
    'Друг 1': {'Треккинговые палки', 'Палатка', 'Спальный мешок', 'Котелок'},
    'Друг 2': {'Палатка', 'Спальный мешок', 'Посуда', 'Фонарик'},
    'Друг 3': {'Треккинговые палки', 'Палатка', 'Спальный мешок', 'Посуда', 'Фонарик'}
}

common, unique, other = find_shared_items(friends)
print("Вещи, которые взяли все три друга:", common)
print("Уникальные вещи, есть только у одного друга:", unique)
print("Вещи, которые есть у всех друзей кроме одного:")
for friend, items in other.items():
    print(friend + ":", items)
