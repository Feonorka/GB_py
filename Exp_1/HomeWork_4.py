#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Введите четверть: ', end=' ')
num = int(input())
while num <= 0 or num > 4:
    print('Введите верное число: ', end=' ')
    num = int(input())

if num == 1:
    print('-X : Y')
if num == 2:
    print('X : -Y')
if num == 3:
    print('-X : -Y')
if num == 4:
    print('X : -Y')