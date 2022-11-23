# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xyz = ["X", "Y", "Z"]
a = []
for i in range(len(xyz)):
    a.append(input(f"Введите значение {xyz[i]}: "))
left = not (xyz[0] or xyz[1] or xyz[2])
right = not xyz[0] and not xyz[1] and not xyz[2]
result = left == right
if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")