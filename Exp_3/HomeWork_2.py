#3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

a = input('Введите число: ')
if isfloat(a):
    print('Это число')
else:
    print('Это не число')