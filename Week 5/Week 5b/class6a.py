from math import sqrt, cos, sin, tan
import numpy as np
import matplotlib.pyplot as plt
def distance(x1, y1, x2, y2):
    
    def square(x):
        return x**2

    return sqrt(square(x1-x2) + square(y1-y2))

print(distance(1,2,3,4))

def f():
    print("hello")
x = f
print(x)

#partial implementation incoming
def make_yell_n(n):
    def yell_n(s):
        return s*n
    return yell_n

#we return yell_n(s): return s*4 when we call make_yell_n(4) here
yell_4 = make_yell_n(4)
print(yell_4('yoyopapayo'))
print(yell_4)
f_1 = cos
print(f_1(0))

#can even store functions into a list, tuple, etc
my_f = [cos, sin, tan, f, len]
print(my_f[4]([1,2,3,4,5,6]))

#we can even input a function into a function - like sin(cos(x))

def do_twice(x):
    x()
    x()
do_twice(f)

def add1to(x):
    return x + 1
def square(x):
    x*x
def do_n_times(f,n,x):
    if n <= 1:
        return f(x)
    else:
        return f(do_n_times(f,n-1,x))
print(do_n_times(add1to, 3, 2))

#lambda calculus
def add1(x):
    return x + 1
func_add1 = lambda x : x + 1
print(func_add1(9) == add1(9))


#def of derv.
def deriv(f):
    dx = 0.0000000001
    return lambda x: (f(x+dx)-f(x))/dx

cos(0.123)
func_sin = deriv(sin)
print(func_sin(.123))

def a(x):
    return x**3 + 3*x + x-1

print(deriv(a)(9))

#newton's method
def newtonM(g):
    x = 999 #doesn't matter
    err = 0.000000000001
    while(abs(g(x))>err):
        x -= g(x)/deriv(g)(x)
    return x

def my_own_sqrt(A):
    return newtonM(lambda x:x*x-A)
x = my_own_sqrt(10)
print(x*x)

#broadcasting for multi-dimensional arrays
#remember to import np.array
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print(a[a<10], a[1,2])

#plotting
x1 = np.linspace(0,3.14,100)
y1 = np.cos(x1)
plt.plot(x1, y1)
plt.show()

x = np.linspace(0, 3.14*4, 100)
y3 = np.sin(x)
y4 = np.cos(x)
plt.plot(x, y3, 'sg', label='sine')
plt.plot(x, y4, '4r', label='cosine')
plt.ylim(-2, 2)

plt.legend(loc='upper right')
plt.title('Sine and Cosine curves')
plt.show()

#multiple plots
#plt.subplot(abc): a = how many rows, b = how many columns, c = which row/column u want to put ur current graph in

plt.subplot(121)
plt.plot(x, y3, '-g')
plt.ylim(-1.5, 1.5)
plt.title('sine curve')
plt.subplot(122)
plt.plot(x, y4,'-b')
plt.ylim(-1.5 ,1.5)
plt.title('cosine curve')
plt.show()