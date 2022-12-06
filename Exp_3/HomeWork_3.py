#3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о".
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
print("Введите строку: ", end=' ')
spisok = [str(i) for i in input()]
search_for = str(input('Введите искомый символ: '))
start = 1
end = len(spisok) - 1
start_pos = 0
end_pos = 0
if search_for not in spisok:
    print("Отсутствует")
elif spisok.count(search_for) == 1:
    print("Искомый элемент один в списке")
else:
    for i in range(len(spisok)):
        if search_for in spisok[:start]:
            start_pos = spisok.index(search_for)
            break
        else:
            start += 1
    for i in range(len(spisok)):
        if search_for in spisok[end:]:
            end_pos = spisok.index(search_for,end)
            break
        else:
            end -= 1
temp_list = spisok[start_pos + 1: end_pos]
spisok[start_pos + 1: end_pos] = temp_list[::-1]
print(spisok)