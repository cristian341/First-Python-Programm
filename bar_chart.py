import matplotlib.pyplot as plt
import numpy as np 
import randomcolor
def bar_chart():
    x = tuple(map(str,input("Enter the x Names separated by space :").split()))
    y = tuple(map(int,input("Enter the y numbers separated by names:").split()))
    rand_color = randomcolor.RandomColor().generate()
    plt.bar(x,y,color =rand_color)
    plt.grid()
    plt.show()

