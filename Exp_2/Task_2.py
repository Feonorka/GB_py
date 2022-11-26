# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(end="")
for k in range(c, d + 1):
    print("\t", k, end="")
print()
for i in range(a, b+1):
    print(i, "", end="")
    for j in range(c, d+1):
        print("\t", end="")
        print(i * j, end="")
    print()