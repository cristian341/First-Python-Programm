import matplotlib.pyplot as plt
import numpy
def pie_chart():
    y = tuple(map(int,input("Enter the numbers:").split()))
    x = tuple(map(str,input("Enter the names: ").split()))
    plt.pie(y,x)
    plt.show()