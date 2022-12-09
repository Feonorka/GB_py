r = lambda a, b: a + b
print(r(3, 5))

r = lambda a, b: a + b if a < b else a - b
print(r(5, 3))

hi = lambda: 'Hi All'
print(hi())