'''
Full Name: TAN YAO HONG, BRYAN
Matric No.: A0171585X
Email: bryantanyh@u.yale-nus.edu.sg
'''

# Complete Q1 below
def describe_data(L):
    for item in L:
        print("The type of the element " + str(item) + " is " + str(type(item)))

# Complete Q2 below
# Remember NOT to use the "count" function!
# No need to be 'deep'
def count(L,x):
    counter = 0
    for item in L:
        if item == x:
            counter += 1
    return(counter)
# Complete Q3 below
# Remember NOT to use the "sort" function!
def largest_three(L):
    if len(L) < 3:
        print('Please insert a list with three or more elements.')
    else:
        stor = [0,0,0]
        for i in range(2, -1, -1):
            stor[i] = max(L)
            L.remove(max(L))
        return(tuple(stor))
            
    
import matplotlib.pyplot as plt
original_wave_sample = [0, 3, 7, 14, 18, 24, 23, 29, 28, 30, 32, 35, 31, 34, 32, 30, 25, 25, 24, 23, 18, 14, 15, 14, 12, 12, 7, 8, 10, 9, 5, 8, 8, 8, 8, 5, 6, 4, 2, 2, 3, -1, -5, -4, -9, -9, -14, -16, -17, -18, -23, -24, -25, -25, -23, -20, -20, -16, -17, -11, -7, -7, 0, 3, 6, 8, 15, 18, 19, 24, 27, 24, 28, 25, 29, 27, 26, 22, 20, 16, 13, 13, 11, 7, 4, 0, 0, 0, 0, -3, -6, -6, -7, -6, -5, -7, -6, -6, -6, -6, -7, -9, -13, -11, -17, -16, -22, -24, -23, -27, -29, -30, -34, -33, -34, -37, -34, -32, -33, -28, -28, -23, -18, -13, -10, -8, 0, 3, 10, 12, 15, 22, 22, 27, 29, 31, 31, 29, 31, 27, 26, 27, 24, 20, 17, 17, 14, 11, 12, 8, 6, 5, 8, 6, 3, 6, 7, 4, 7, 6, 7, 6, 5, 4, 2, 0, -2, -3, -6, -7, -12, -14, -16, -15, -18, -21, -22, -23, -26, -26, -22, -23, -21, -18, -13, -9, -8, -3, -1, 6, 10, 12, 17, 20, 23, 25, 28, 30, 30, 30, 27, 25, 26, 24, 19, 18, 17, 12, 12, 8, 7, 4, 0, -2, -2, -1, -1, -6, -4, -4, -3, -5, -7, -8, -5, -5, -7, -10, -10, -12, -17, -17, -22, -21, -25, -29, -29, -32, -35, -34, -32, -33, -33, -33, -33, -28, -24, -22, -18, -15, -9, -6, 0, 6, 9, 11, 16, 22, 22, 24, 25, 29, 30, 31, 28, 29, 27, 22, 22, 20, 16, 17, 15, 14, 10, 10, 6, 8, 4, 4, 7, 4, 7, 7, 6, 6, 3, 7, 2, 2, 4, 1, 0, -2, -3, -7, -8, -13, -14, -16]
t = [i for i in range(len(original_wave_sample))]

''' Uncomment next 2 lines to show plot '''
#plt.plot(t,original_wave_sample)
#plt.show()

# Question 4
def detect_noise(wave):
    signal_noise, gap_noise = [], []
    for i in range(0, len(wave)):
        if wave[i] > 34 or wave[i] < -34:
            signal_noise.append((i, wave[i]))
    for i in range(1, len(wave)-1):
        if abs(wave[i] - wave[i+1]) > 6:
            gap_noise.append((i, i+1, wave[i], wave[i+1]))
    if signal_noise or gap_noise:
        print("Noise(s) detected!")
        for item in signal_noise:
            print("Signal out of bound at position " + str(item[0]) + " with value " + str(item[1]))
        for item in gap_noise:
            print("The gap is too big between the positions at " + str(item[0]) + " and " + str(item[1]) + ' with values ' + str(item[2]) + ' , ' + str(item[3]))
    else:
        print("No noise detected!")

# Question 5
def repair_signal(wave):
    #include first element of wave into new_sig_l
    new_sig_l = [wave[0]]
    for i in range(1, len(wave)-1):
        if wave[i] > 34 or wave[i] < -34:
            new_sig = (wave[i-1] + wave[i+1])/2
            new_sig_l.append(new_sig) 
        elif abs(wave[i] - wave[i+1]) > 6:
            new_sig = (wave[i-1] + wave[i+1])/2
            new_sig_l.append(new_sig)
        else:
            new_sig_l.append(wave[i])
    #include last element of wave into new_sig_l since the for-loop excludes it
    new_sig_l.append(wave[len(wave)-1])
    return(new_sig_l)
    
''' TESTING '''
print('Detecting noise in the original signal')
detect_noise(original_wave_sample)
new_signal = repair_signal(original_wave_sample)
print()
print('Detecting noise in the repaired signal')
detect_noise(new_signal)
print()
print('Detecting noise in the original signal again')
detect_noise(original_wave_sample)

'''Testing for other questions
if __name__ == '__main__':
    input_list = [3.145, True, 42, '88', (1,3)]
    describe_data(input_list)
    A, B = [5,2,1,'5',9,5,True], [1,(5,3),True]
    print(count(A, 5))
    print(count(B, 5))
    a,b,c = largest_three([9,8,7,6,5,4,3,2,1]), largest_three([1,2,3]), largest_three([-1,-2,-3,-4])
    print(a,b,c)
'''
