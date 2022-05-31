

def happy_number():
    num = int(input("Enter a number: "))
    n = num
    Sum = 0
    ans = False
    
    while Sum != 1 and Sum != 4: # Outer loop
        Sum = 0
        while n > 0:  # Inner loop
            digit = n % 10
            Sum  = Sum + digit ** 2
            n = n // 10
        n = Sum
        if Sum == 1:
            ans = True
    if ans == True:
        print(num," is a happy number :^) ")
    else:
        print(num," is a sad number :^( ")
happy_number()










