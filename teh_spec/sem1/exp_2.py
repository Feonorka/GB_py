num = int(input("Enter a number: "))

if num <= 1 or num > 100000:
    print("Invalid input")
elif num == 2:
    print("The number is prime")
else:
    is_prime = True
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("The number is prime")
    else:
        print("The number is composite")