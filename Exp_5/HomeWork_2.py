#Крестики-нолики
dicto = {'Линкор': [['З6'], ['А3'], ['З4'], ['Б4']], 'Крейсер': [['Ж7', 'А3'], ['Ж6', 'Д3'], ['И4', 'Д5']], 'Эсминец': [['Б6', 'Ж7', 'Е7'], ['К7', 'И8', 'Ж4']], 'Катер': [['Б2', 'Ж5', 'Ж9', 'К7']]}
my_list = []

for ship in dicto:
    for ds in dicto[ship]:
        for lm in ds:
            my_list.append(lm) 

print(my_list)
print('А3' in dicto.values())
print('А3' in my_list)

