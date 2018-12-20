from math import sqrt 
def distance(x1, y1, x2, y2): 
    return sqrt(square(x1-x2)+square(y1-y2))

def square(x):
    return x*x