# class Fruits:
#     pass
# a = Fruits()
# b = Fruits()

# a.name = 'apple'
# a.weight = 120

# b.name = 'orange'
# b.weight = 150

# print(a.name, a.weight)
# print(b.name, b.weight)

# b.weight -= 50

# print(a.name, a.weight)
# print(b.name, b.weight)

# class Hellow:
#     def hello_world(self):
#         print('Привет, мир!')

# great = Hellow()
# great.hello_world()

# class Car:
#     def __init__(self, color):
#         self.e_on = False
#         self.color = color
#     def start(self):
#         self.e_on = True
#     def drive_on(self, city):
#         if self.e_on:
#             print(f'Едем в {city} на {self.color} автомобиле')
#         else:
#             print('Не едем')

# s = Car('Красный')
# s.start()
# s.drive_on('Сочи')

# print (1 + 2)

# class Books:
#     def __init__(self, name, auth):
#         self.name = name
#         self.auth = auth
#     def get_name(self):
#         return self.name
#     def get_auth(self):
#         return self.auth

# book = Books('Война и мир', 'Лев Толстой')

# print(f'книга - {book.get_name()}, автор - {book.get_auth()}')

###
#class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def perimeter(self):
#         return  2 * pi * self.radius
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
#     def perimeter(self):
#         return 4 * self.side
#
#
#
# def print_shape_info(shape):
#     print(f'Area = {shape.area()}, perimeter = {shape.perimeter()}')
#
# square = Square(10)
# # print(square.area())
# # print(square.perimeter())
# print_shape_info(square)
#
# circle = Circle(10)
# print_shape_info(circle)
