# 1) Есть список:  s = ['a', 'b', 'c', 'd', 'e']
# Необходимо написать программу, которая сдвинет список spisok следующим образом: ['c', 'd', 'e', 'a', 'b']

lst = ['a', 'b', 'c', 'd', 'e']
print(lst)
dis_to = int(input())

for i in range(dis_to):
    temp = lst.pop(0)
    lst.append(temp)
print(lst)