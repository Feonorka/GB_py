# 5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
def GCD_Loop( a, b): 
    if a > b:  # define the if condition 
        temp = b 
    else: 
        temp = a 
    for i in range(1, temp + 1): 
        if(( a % i == 0) and(b % i == 0 )): 
            gcd = i 
    return gcd 
x = int(input(" Enter the first number: ") ) # take first no.  
y =int(input(" Enter the second number: ")) # take second no.  
num = GCD_Loop(x, y) # call the gcd_fun() to find the result 
print("GCD of two number is: ") 
print(num) # call num