import matplotlib.pyplot as plt
import numpy as np

def line_graphs(**kwargs):
    x1 = tuple(map(int,input("Enter the x numbers:").split()))
    y1 = tuple(map(int,input("Enter the y numbers:").split()))
    font1 ={'family':'serif','color':'blue','size':20}
    font2 ={'family':'serif','color':'yellow','size':15}
    #rand_color = randomcolor.RandomColor().generate()
    plt.title(input("Enter the title of line graph:"),fontdict = font1)
    plt.xlabel(input("Enter the x axis title:"),fontdict = font2)
    plt.ylabel(input("Enter tthe y axis title:"),fontdict = font2)
    
    plt.plot(x1,y1)
    plt.grid()
    plt.show()





