# Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

x = int(input('Введите число:'))
while x < 10 and x > 0:
    x = int(input('Введите многозначное число:'))

spisok = list(map(int, str(x)))

for i in range(len(spisok)):
    if i == len(spisok) - 1:
        break
    if spisok[i] < spisok[i + 1]:
        result = 'Да'
    else:
        result = 'Нет'
        break
print(result)