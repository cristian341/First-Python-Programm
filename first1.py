#x2= tuple(map(int,input("Enter the x numbers:").split()))
#y2 = tuple(map(int,input("Enter the y numbers:").split()))
#plt.plot(x1,y1,'-k')
#plt.plot(x2,y2,'o:r')
import randomcolor
rand = randomcolor.RandomColor()
var =str(rand.generate())[1:-1]
#var = str(var)[1:-1]
var = var.replace("'",'"')
print(var)