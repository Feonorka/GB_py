# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
kassa_dict = {25: 4, 10: 10, 3: 30, 1: 100}
polychka = 0

def inventory(data):
  lis = []
  lis = [key* val for key, val in data.items()]
  return lis

def zp_money(dict_of_limit, sum):
    money_dict = dict()
    
    return money_dict

kassa_limit_money = inventory(kassa_dict)
money_limit = sum(kassa_limit_money)
print(money_limit)

zp = int(input('Введите число: '))

if zp > money_limit:
    print('В кассе недостаточно средств чтобы выдать Вам зарплату, обратитесь в бухгалтерию. Спасибо!')
    exit
else:
    print(zp_money(kassa_dict, zp))

# salary = int(input('Write salary: '))
# salary_help = salary
# bills = [0, 0, 0, 0]
# F = []
# F.append(0)
# bills_count = 4
# bills_nominal = [25, 10, 3, 1]
# n = salary
# for i in range(1, n + 1, 1):
#     F.append(100000)
#     for j in range(bills_count):
#         if i >= bills_nominal[j] and F[i - bills_nominal[j]] + 1 < F[i]:
#             F[i] = F[i - bills_nominal[j]] + 1

# while n > 0:
#     for i in range(bills_count):
#         if F[n - bills_nominal[i]] == F[n] - 1:
#             bills[i] += 1
#             n -= bills_nominal[i]
#             break

# print(f'Salary {salary} can be paid as: 25: {bills[0]}, 10: {bills[1]}, 3: {bills[2]}, 1: {bills[3]}')
