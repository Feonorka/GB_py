# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))
my_list = list()
res = 1

for i in range(num):
    res *= (i + 1)
    my_list.append(res)
print(my_list)