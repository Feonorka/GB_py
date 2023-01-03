# 2)Делаем программу , где используем классы.
# Где класс будет содержать имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список студентов.
# После выводим список , отсортированный по имени, потом выводятся студенты, имеющие неудовлетворительные оценки.
class Student_name:
    name = 'no'
    def init(self, n):
        self.name = str(n)
class Group:
    group = 'no'
    def init(self, g):
        self.group = str(g)
class Point:
    poin = 0
    def init(self, p):
        self.point = int(p)

n1 = Student_name(input().split(" "))
g1 = Group(['CX - 11', 'YX - 22', 'BV - 33'])
p1 = Point(int(input()))
point_dict = {}
for i in n1.name:
    point_dict[i] = p1.point

print(point_dict)