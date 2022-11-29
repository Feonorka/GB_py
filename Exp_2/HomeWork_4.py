# Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

x = int(input('Введите число:'))
count = 0
num = x
result = 'Да'
while x < 10 and x > 0:
    x = int(input('Введите многозначное число:'))

while num != 0:
    num = num // 10
    count += 1
print(f'Длина числа составляет {count} знака')
for i in range(count, 1, ):
    low = x // 10 ** (count - i)
    ost_low = x % 10 ** (count - i)
    next = ost_low // 10 ** (count - (i + 1))
    print(low)
    print(ost_low)
    print(next)