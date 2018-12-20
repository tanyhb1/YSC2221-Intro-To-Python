import matplotlib.pyplot as plt
from math import cos


def factorialR(n):
    if n == 1:
        return(1)
    else:
        return(n*factorialR(n-1))
    
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_tail(n):
    def fib_helper(a, b, n):
        return(fib_helper(b, a+b, n-1)) if n > 0 else a
    return fib_helper(0, 1, n)

even_no = [0,2,4,6,8,10]
friends = ['yo', 'hello', 'fuck',5]
friends.append(even_no)

a_list = []
for i in range(0,101):
    a_list.append(i)
    
b_list = [i*i for i in range(1,11)]

c_list = [i for i in range(1,101,2)]

x = [i for i in range(1,101)]
y = [i*i for i in range(1,101)]

x = [i/100 for i in range(0,314)]
y = [cos(i) for i in x]


nonprime = [j for i in range(2,8) for j in range(i*2, 50, i)]
prime = [x for x in range(1,50) if x not in nonprime]
if __name__ == '__main__':
    print(nonprime)
    print(prime)
