test1 = '((4-((1+2)+3)))'
test2 = '(1+2)-(3+4)+(5-6)-(7-8)'
test3 = '((1+2)-(5+7))'
test4 = '((1+2)-(5+7))-('
test5 = '(1+2-3+[4+5]-(5+[6+7]))'
test6 = '(()[]][)'
test7 = '(()[(][)])'

def filterParentheses(s):
    new_s = ''
    paren_l = '()[]'
    for x in s:
        if x in paren_l:
            new_s += x
    return new_s
        
def checkParentheses(s):
    #counter-based method since we are only concerned with one type of parentheses
    parentheses = 0
    for x in filterParentheses(s):
        if parentheses < 0:
            return False
        elif x == '(':
            parentheses += 1
        elif x == ')':
            parentheses -= 1
    return (parentheses == 0)

def checkMoreParentheses(s):
    #stack-based method since we are concerned with more than one type of parentheses
    #create dictionary of the parentheses concerned
    paren_map = {'(':')', '[':']'}
    parentheses = []
    for x in filterParentheses(s):
        #if x is either ( or [, append its closing bracket ) or ] to parentheses
        if x in paren_map:
            parentheses.append(paren_map[x])
        #if x is ) or ], check that parentheses is non-empty and that x is equivalent to the most 
        #recent closing bracket at the top of the stack (to ensure mathematical correctness)
        #while removing it from the stack. If not, return False
        elif not (parentheses and x == parentheses.pop()):
            return False
    #after all iterations, check if parentheses is still non-empty. If non-empty, return false.
    #if empty, return true.
    if parentheses:
        return False
    else:
        return True
            


print(filterParentheses(test1))
print(filterParentheses(test2))
print(filterParentheses(test3))
print(filterParentheses(test4))
print(filterParentheses(test5))
print(filterParentheses(test6))
print(filterParentheses(test7))
print(checkParentheses(test1))
print(checkParentheses(test2))
print(checkParentheses(test3))
print(checkParentheses(test4))
print(checkParentheses(test5))
#test 6 will be true for checkParentheses (since we consider only '(' and ')') but false for checkMoreParentheses
print(checkParentheses(test6))
#test7 will be true for checkParentheses but false for checkMoreParentheses
print(checkParentheses(test7))
test = '(1+2-3+[4+5]-(5+[6+7]))'
print('Check for more parentheses')
print(checkMoreParentheses(test5))
print(checkMoreParentheses(test6))
print(checkMoreParentheses(test7))
print(checkMoreParentheses(test))
test = '(1+2-3+[4+5]-(5+[6+7])'
print(checkMoreParentheses(test))
test = '(1+2-3+[4+5]-(5+[6+7]))[(])'
print(checkMoreParentheses(test))
test = '(1+2-3+[4+5]-(5+[6+7]))[]()((()))[[[((1+3)*5)]]]'
print(checkMoreParentheses(test))
