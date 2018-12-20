from math import *

def square(x):
    return x * x

def addTwoNumbers() :
    a = int(input('Enter an integer\n'))
    b = int(input('Enter another integer:\n'))
    print('The sum is:')
    print(a+b)

def sum_of_squares(x,y):
    return square(x) + square(y)
def hypotenuse(a,b):
    return sqrt(sum_of_squares(a,b))

def quadratic_solver(a, b, c):
    det = b**2 - 4*a*c
    if det < 0 :
        print("no real roots")
    else : 
        sol1 = (-b + sqrt(det)) / (2*a)
        sol2 = (-b - sqrt(det)) / (2*a)
        print('The two roots are ' + str(sol1) + ' and ' + str(sol2))
    
def factorial(n):
    if n < 1:
        return 0
    else:
        ans = 1
        i = 1
        while i <= n:
            ans = ans * i
            i = i + 1
        print(ans)
        
def factorialr(n):
    if n < 1:
        return 1
    else:
        x = factorialr(n-1) * n
        print(str(n) + '! = ' + str(x))
        return x
if __name__ == '__main__':
    factorialr(5)
    
