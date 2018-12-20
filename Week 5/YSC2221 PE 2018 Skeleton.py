'''
Names: TAN YAO HONG BRYAN
Student Number: A0171585X
'''

#The following lists are sample test cases for Problem 1a,b and c
names = ('Peter','John',
        'Mary','Paul','Richard','Anne','Zoe','Carl','Kelvin')
Eng_scores = (80,90,70,50,99,75,65,99,100)
Math_scores = (77,55,49,88,100,57,80,90,50)
Sci_scores = (44,66,45,78,90,80,66,100,56)

#For Problem 1a,b and c, you can assume all the given lists have
#the same length with each other.
#And the scores are all integers and the names are all strings

#Problem 1a
def print_total_scores(names,Eng_s,Math_s,Sci_s):
    l = []
    for i in range(0, len(names)):
        score = Eng_s[i] + Math_s[i] + Sci_s[i]
        name = names[i]
        item = (name, score)
        l.append(item)
    for i in range(0, len(l)):
        print(l[i][0] + ' ' + str(l[i][1]) )


print("<<All total scores>>")
print_total_scores(names, Eng_scores, Math_scores, Sci_scores)


#Problem 1b
def print_total_scores_sorted(names,Eng_s,Math_s,Sci_s):
    l = []
    for i in range(0, len(names)):
        score = Eng_s[i] + Math_s[i] + Sci_s[i]
        name = names[i]
        item = (name, score)
        l.append(item)
    l.sort()
    for i in range(0, len(l)):
        print(l[i][0] + ' ' + str(l[i][1]) )


print("\n<<All total scores sorted by names>>")
print_total_scores_sorted(names, Eng_scores, Math_scores, Sci_scores)


#Problem 1c   
def show_max_scores(names, Eng_s, Math_s, Sci_s):
    l, max_l = [], []
    for i in range(0, len(names)):
        score = Eng_s[i] + Math_s[i] + Sci_s[i]
        name = names[i]
        item = (score, name)
        l.append(item)
    l.sort()
    curr = max(l)
    l.remove(curr)
    max_l.append(curr)
    while(True):
        stor = max(l)
        if stor[0] < curr[0]:
            break
        else:
            max_l.append(stor)
            l.remove(stor)
            curr = stor
    for i in range(0, len(max_l)):
        print(max_l[i][1] + ' has the maximum score of ' + str(max_l[i][0]))
        

print("\n<<The top student(s)>>")
show_max_scores(names, Eng_scores, Math_scores, Sci_scores)

#Problem 2
#sample test cases
weights = (75,80,90,77,88,91,60,74,73,70,55,93,59)

def searchCouple(L,n):
    stor = []
    for i in range(0, len(L)):
        for j in range(i+1, len(L)):
            A = L[i] + L[j]
            if A == n:
                if L[i] < L[j]:
                    stor.append((L[i], L[j]))
                else:
                    stor.append((L[j], L[i]))
    return stor

print(searchCouple(weights,150))
print(searchCouple(weights,152))
print(searchCouple(weights,199))

        
        

        
    
