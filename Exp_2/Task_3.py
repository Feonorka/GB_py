# 3) Решить следующую задачу, проверки знания таблицы умножения. Программа выводит 10 примеров и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три. 
# Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
# В итоге выводим количество верных ответов и оценку
import random
count = 0
for exp in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = int(input(f'{num1} * {num2} = '))
    if answer == num1 * num2:
        count += 1
if count == 10: print('Оценка пять!')
elif count >= 7 and count < 10: print('Оценка четыре!')
else: print('Оценка три...')
