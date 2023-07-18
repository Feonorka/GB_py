def calc_fraction(frac1, frac2):
    numerator1, denominator1 = frac1.split('/')
    numerator2, denominator2 = frac2.split('/')
    
    numerator_sum = int(numerator1) * int(denominator2) + int(numerator2) * int(denominator1)
    denominator_sum = int(denominator1) * int(denominator2)
    
    numerator_prod = int(numerator1) * int(numerator2)
    denominator_prod = int(denominator1) * int(denominator2)
    
    return f"Сумма: {numerator_sum}/{denominator_sum}, Произведение: {numerator_prod}/{denominator_prod}"

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

result = calc_fraction(fraction1, fraction2)
print(result)