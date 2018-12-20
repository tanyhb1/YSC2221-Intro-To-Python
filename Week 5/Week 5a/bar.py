import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000
def roll_dice():
    return random.randint(1,6)

dice_stat = []
for i in range(N):
    dice_stat.append(roll_dice() + roll_dice() + roll_dice())
    
plt.hist(dice_stat, 16)
plt.show()