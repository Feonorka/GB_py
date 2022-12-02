# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
kassa_dict = {25: 40, 10: 100, 3: 300, 1: 1000}
polychka = 0

def inventory(data):
  lis = []
  lis = [key* val for key, val in data.items()]
  return lis

def zp_money(dict_of_limit, sum_zp):
    money_dict = dict()
    temp_sum = 0
    
    for key in dict_of_limit:
        temp_lim = int(dict_of_limit[key])
        count = 0
        while temp_sum <= sum_zp:
            if count <= temp_lim:
                if temp_sum + key <= sum_zp:
                    temp_sum += key
                    count += 1
                    money_dict[key] = count
                else:
                    break
            else:
                break
    return money_dict

kassa_limit_money = inventory(kassa_dict)
money_limit = sum(kassa_limit_money)
print(money_limit)
print(kassa_limit_money)
zp = int(input('Введите число: '))

if zp > money_limit:
    print('В кассе недостаточно средств чтобы выдать Вам зарплату, обратитесь в бухгалтерию. Спасибо!')
    exit
else:
    print(zp_money(kassa_dict, zp))