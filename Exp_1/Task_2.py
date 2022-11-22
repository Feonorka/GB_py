my_spisok = [int(i) for i in input().split()]

max_num = 0
for i in range(len(my_spisok)):
    if my_spisok[i] > max_num:
        max_num = my_spisok[i]
        i += 1
    else:
        i += 1
print(max_num)