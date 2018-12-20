import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
type('asdas')
input_list = [3.1415, True, 42, '88', (1,3)]
describe_data(input_list)
def describe_data(L):
    for item in L:
        print("The type of the element " + item + " is " + type(item))
describe_data
describe_data(input_list)
