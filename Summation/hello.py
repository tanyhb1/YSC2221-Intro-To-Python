def sum_list(l):
    counter = 0
    for i in l:
        counter += i
    print(counter)

def sum_list_r(l):
    if not l:
        return 0
    else:
        return l[len(l)-1] + sum_list_r(l[:len(l)-1])

    
def sort(x):
    if len(x) == 1:
        return(x)
    else:
        middle = len(x)/2
        left = sort(x[:int(middle)])
        right = sort(x[int(middle):])
        
        return(merge(left, right))
        
def merge(left, right):
    i, j = 0, 0
    c = []

    while(len(c) < len(left) + len(right)):
        if left[i] < right[j]:
            c.append(left[i])
            i = i + 1
        else:
            c.append(right[j])
            j = j + 1
        if i == len(left) or j == len(right):
            c.extend(left[i:] or right[j:])
            break
    return(c)


def ChoosePivot():
    
def QuickSort(l):
    pivotindex = ChoosePivot(l)
    l[0], l[pivotindex] = l[pivotindex], l[0]
    i_bound, uni_bound = 1, 1
    for i in range(1, len(l)):
        if 
