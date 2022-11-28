#3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.
text = input('Введите текст: \n')
lowel = 'уеоаыяиюэё'
consonant = 'цкнгшщзйхфвпрлджчсмтб'
count_low = 0
count_cons = 0
for i in text:
    if i in lowel:
        count_low += 1
    elif i in consonant:
        count_cons += 1
print(f'Количество гласных: {count_low} \nКоличество согласных: {count_cons}')
