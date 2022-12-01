#3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором
import random
def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        smallest = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
 
spisok = [random.randint(-5, 5) for x in range(random.randint(1, 10))]

selection_sort(spisok)
print('Отсортированный список: ', end='')
print(spisok)