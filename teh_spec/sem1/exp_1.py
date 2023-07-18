a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print("The triangle is scalene")
        elif a == b and a == c:
            print("The triangle is equilateral")
        else:
            print("The triangle is isosceles")
    else:
        print("The triangle cannot be formed")
else:
    print("Invalid input")