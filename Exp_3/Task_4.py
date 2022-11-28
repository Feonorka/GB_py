#3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами
text = input('Введите текст: ')
count = len(text)
text1 = text[:count//2]
if not count % 2:
    print(text2 + text1)
else:
    text2 = texxt[:count//2]
    text2 = text[count//2:]
    print(text2 + text[count//2 + 1] + text1)
