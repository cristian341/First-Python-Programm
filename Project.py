import math
from statistics import mode
from graphics import *
from bar_chart import *
from pie_chart import *
def area_of_square(x):
    return print(f"Area of square is {round(x**2, 3)}cm²")

def perimeter_of_square(x):
    return print(f"Perimeter of square is {round(4*x, 3)}cm")

def volume_of_cube(x):
    return print(f"Volume of cube is {round(x**3, 3)}cm³")

def volume_of_cuboid(a,b,c):
    return print(f"Volume of cuboid is {round(a*b*c, 3)}cm³")

def perimeter_of_rectangular(l,w):
    return print(f"Perimeter of rectangular is {round((l*2)+(w*2), 3)}cm")

def area_of_rectangular(l,w):
    return print(f"Area of rectangular is {round(l*w, 3)}cm²")

def area_of_triangle(b,h):
    return print(f"Area of triangle is {round((b*h)/2, 3)}cm²")

def volume_of_triangle(b,h,H):
    return print(f"Volume of trinagle is {round(((b*h)/2)*H, 3)}cm³")

def area_of_circle(r):
    return print(f"Area of circle is {round(math.pi*r**2, 3)}cm²")

def diagonal_of_square(x):  #new
    d = x*math.sqrt(2)
    return print(f"Diagonal of square is {round(d, 3)}cm")

def diagonal_of_rectangular(l,w): #new
    d = math.sqrt((l**2)+(w**2))
    return print(f"Diagonal of rectangular is {round(d, 3)}cm")

def circumference_of_circle(r):
    return print(f"Circumference of circle is {round((math.pi*r)*2, 3)}cm")

def area_of_kite(w,l):
    return print(f"Area of kite is {round(0.5*w*l, 3)}cm")

def area_of_trapezium(a,b,h):
    return print(f"Area of trapezium is {round((h*(a+b))/2, 3)}cm2")

def volume_of_cylinder(r,h):
    return print(f"Volume of cylinder is {round(math.pi*(r**2)*h, 3)}cm3")

def volume_of_triangular_prism(b,h,l):
    return print(f"Volume of triangular prism is {round((b*h*l)/2, 3)}cm3")

def vol_square_based_pyramid(x,h):
    return print(f"Volume of square based pyramid is {round(((x**2)*h)/3, 3)}cm3")

def area_of_sphere(r):
    return print(f"Area of shpere is {round(4*math.pi*pow(r,2),3)}cm²")

def volume_of_sphere(r):
    return print(f"Volume of shpere is {round(4/3*math.pi*pow(r,3),4) }cm³")

def volume_of_cone(r,h):
    return print(f"Volume of Cone is {round(1/3*math.pi*pow(r,2)*h,4)}cm³")
####################################################################### Algebra
def adding(x,y):
    return print(f"The sum of x and y is {x+y}")

def subtract(x,y):
    return print(f"The subtract of x and y is {x-y}")

def multiply(x,y):
    return print(f"The multiply of x and y is {x*y}")

def division(x,y):
    return print(f"The division of x and y is {x/y}")

def floor_div(x,y):
    return print(f"The floor division of x and y is {x//y}")

def exponential(x,y):
    return print(f"The exponential of x and y is {x**y}")

def modulus(x,y):
    return print(f"The rest of y in x is {x % y}")
#############################################################Formulas
def one(a,b):
    return print(f"The result of ({a}+{b})² is = {(a**2)+(b**2)+2*a*b}")

def two(a,b):
    return print(f"The result of ({a}-{b})² is = {(a**2)+(b**2)-2*a*b}")

def three(a,b):
    return print(f"The result of({a}²+{b}²) is = {((a+b)**2)-2*a*b}")

def four(a,b):
    return print(f"The result of({a}²-{b}²) is = {(a+b)*(a-b)}")

def five(a,b):
    return print(f"The result of({a}³+{b}³) is = {pow((a+b),3)-3*a*b*(a+b)}")

def six(a,b):
    return print(f"The result of({a}³-{b}³) is = {pow((a-b),3)+3*a*b*(a-b)}")

def seven(a,b):
    return print(f"The result of 2({a}²+{b}²) is = {pow((a+b), 2)+pow((a-b), 2)}")

def eight(a,b):
    return print(f"The result of ({a}+{b})²-({a}-{b})² is = {4*a*b}")

def nine(a,b):
    return print(f"The result of {a}^4+{b}^4  is = {pow(a, 4) + pow(b, 4)}")

def ten(a,b,c):
    return print(f"({a}+{b}+{c})²= {pow(a,2)+pow(b,2)+pow(c,2)+2*a*b+2*b*c+2*c*a}")

def eleven(a,b,c):
    return print(f"({a}+{b}-{c})²= {pow(a,2)+pow(b,2)+pow(c,2)+2*a*b-2*b*c-2*c*a}")

def twelve(a,b,c):
    return print(f"({a}-{b}-{c})²= {pow(a,2)+pow(b,2)+pow(c,2)-2*a*b+2*b*c-2*c*a}")

##############################################################################Square Root
def power(a,b):
    return print(f"{a} power {b} is {pow(a,b)}")
#######################################################Percentage
def found_the_procent(a,b):
    return print(f"{b}% from {a} is {(a*b/100)} ")

def percentage_increase(a,b):
    return print(f"{a} increased by {b}% is {(a*b/100)+a}")

def percentage_decrease(a,b):
    return print(f"{a} increased by {b}% is {a*(100-b)/100}")

def percentage_difference(a,b):
    if a >= b:
        print(f"Difference between {a} and {b} in percentage is {100-((b*100)/a)}%")
    else:
        print(f"Difference between {a} and {b} in percentage is {((b*100)/a )-100}%")

#def compound_interes(a,b,c):
    #part_one = 1 + b/100
    #amound = a*pow(part_one,c)
    #print(amound)

def compound_interes(a,b,c):
    for i in range(c):
        d= a*(b/100)
        a += d
        print(a)
##################################################################Convertor
def mm(a):
    return print(f"{a}mm in is {a/10}cm,{a/100}dm,{a/1000}m,{a/pow(10,6)}km")

def cm(a):
    return print(f"{a}cm in is {a*10}mm,{a/10}dm,{a/100}m,{a/pow(10,5)}km")

def dm(a):
    return print(f"{a}dm in is {a*100}mm,{a*10}cm,{a/10}m,{a/pow(10,4)}km")

def metre(a):
    return print(f"{a}m in is {a*1000}mm,{a*100}cm,{a*10}dm,{a/1000}km")

def km(a):
    return print(f"{a}km in is {a*pow(10,6)}mm,{a*pow(10,5)}cm,{a*pow(10,3)}dm,{a*1000}m")
############################################################################################Mode
def my_mode():
    list_of_numbers = list(map(int, input("Enter the numbers separeted by space:").split()))
    print(f"The most often number is {mode(list_of_numbers)}")
##################################################################App function
def project_app():
###################################################################First UI
    print(""" 
Choose
0:Geometry
1:Algebra
2:Algebraic Formulas
3:Rounding
4:Mean 
5:Range
6:Square Root
7:Percentage
8:Lenght convertor
9:Mode in a list of numbers
10:Graphs
Type 101 to exit 
    """)
    choose_first = int(input(":"))
###################################################################Second UI
    if choose_first == int(0):
        print("""
0:Area of Square(x) 
1:Perimeter of Square(x)
2:Diagonal of Square(x) 
3:Volume of Cube(x) 
4:Area of Rectangular(l,w)
5:Perimeter of Rectangular(l,w)
6:Diagonal of Rectangular(l,w)
7:Volume of Ruboid(a,b,c) 
8:Area of Rriangle(b,h)
9:Volume of Rriangle(b,h,H)
10:Volume of Rriangular Prism(b,h,l)
11:Volume of Rquare Based Pyramid(x,h) 
12:Area of Circle(r)
13:Circumference of Circle(r)
14:Volume of Clinder(r,h)
15:Area of Kite(w,l)
16:Area of Trapezium(a,b,h)
17:Area of Sphere(r)
18:Volume of Sphere(r)
19:Volume of Cone(r,H)
Type 101 to exit 

        """)
#################################################################################
        var = int(input("Enter the number of operation you want to do  : "))

        if var == int(0):              #0:area_of_square(x) 
            print("You're doing area of square")
            x = float(input("Press the number: ")) 
            area_of_square(x)
            
        

        elif var == int(1):            #1:perimeter_of_square(x)
            print("You're doing perimeter of square")
            x = float(input("Press the number: "))
            perimeter_of_square(x)
            

        elif var == int(2):            #2:Diagonal of square(x)
            print("You're doing the diagonal of square")
            x = float(input("Press the number: "))
            diagonal_of_square(x)
            
        elif var == int(3):           #2:volume_of_cube(x)
            print("You'are doing volume of cube")
            x = float(input("Press the number: "))
            volume_of_cube(x)
            
        elif var == int(4):          #5:area_of_rectangular(l,w)
            print("You'are doing area of rectangular")
            l = float(input("Press lenght: "))
            w = float(input("Prees width: "))
            area_of_rectangular(l,w)
            
        elif var == int(5):            #4:perimeter_of_rectangular(l,w)
            print("You'are doing perimeter of rectangular")
            l = float(input("Press lenght: "))
            w = float(input("Prees width: "))
            perimeter_of_rectangular(l,w)
            
        elif var == int(6):     #6:Diagonal of rectangular(l,w)
            print("You're doing diagonal of rectangular")
            l = float(input("Press lenght: "))
            w = float(input("Press width: "))
            diagonal_of_rectangular(l,w)
            
        elif var == int(7):           #3:volume_of_cuboid(a,b,c)
            print("You'are doing volume of cuboid")
            a = float(input("Press a:"))
            b = float(input("Press b: "))
            c = float(input("Press c: "))
            volume_of_cuboid(a,b,c)
            
        elif var == int(8):          #6:area_of_triangle(b,h)
            print("You'are doing area of triangle")
            b = float(input("Press base: "))
            h = float(input("Press height: "))
            area_of_triangle(b,h)
            
        elif var == int(9):        #7:volume_of_triangle(b,h,H)
            print("You'are doing volume of triangle")
            b = float(input("Press base: "))
            h = float(input("Press height: "))
            H = float(input("Press Height: "))
            volume_of_triangle(b,h,H)
            
        elif var == int(10):   #Volume of triangular prism(b,h,l)
            print("You're doing volume of triangular prism")
            b = float(input("Press base: "))
            h = float(input("Press h: "))
            l = float(input("Press lenght: "))
            volume_of_triangular_prism(b,h,l)
            
        elif var == int(11):  #Volume of square based pyramid(x,h)
            print("You're doing volume of square based pyramid")
            x = float(input("Press x: "))
            h = float(input("Press h: "))
            vol_square_based_pyramid(x,h)
            
        elif var == int(12):         #8:area_of_circle(r)
            print("You'are doing area of circle")
            r = float(input("Press radius: "))
            area_of_circle(r)
            
        elif var == int(13):       # :Circumference of circle(r)
            print("You're doing circumference of circle")
            r = float(input("Press radius: "))
            circumference_of_circle(r)
            
        elif var == int(14):           # Volume of cylinder(r,h)
            print("You're doing volume of cylinder")
            r = float(input("Press radius: "))
            h = float(input("Press h:"))
            volume_of_cylinder(r,h)
            
        elif var == int(15):         # Area of kite(w,l)
            print("You're doing area of kite")
            w = float(input("Press w: "))
            l = float(input("Press l: "))
            area_of_kite(w,l)
            
        elif var == int(16):
            print("You're doing area of trapezium") 
            a = float(input("Press a:"))
            b = float(input("Press b: "))
            h = float(input("Press h:"))
            area_of_trapezium(a,b,h)

        elif var == int(17):
            print("You are doing area of shpere")
            r = float(input("Enter the r:"))
            area_of_sphere(r)
        elif var == int(18):
            print("You are going volume of sphere")
            r = float(input("Enter the r:"))
            volume_of_sphere(r)
        elif var == int(19):
            print("Your are doing Volume of Cone")
            r = float(input("Enter the r:"))
            h = float(input("Press H:"))
            volume_of_cone(r,h)

        elif var == int(101):
            exit()   
    ################################################Fhird UI
    elif choose_first == int(1):
        print("Operation available: \n0: + \n1: - \n2: * \n3: / \n4: // \n5: ** \n6:% \nType 101 to exit  ")
        var_1 = int(input("Enter the number of operation you want to do  : ")) 
        if var_1 == int(0):
            print("You're doing addition")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            adding(x,y)
            
        elif var_1 == int(1):
            print("You're doing subtraction")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            subtract(x,y)
            
        elif var_1 == int(2):
            print("You're doing multiplication")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            multiply(x,y)
            
        elif var_1 == int(3):
            print("You're doing  division")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            division(x,y)
            
        elif var_1 == int(4):
            print("You're doing floor division")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            floor_div(x,y)
            
        elif var_1 == int(5):
            print("You're doing exponential")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            exponential(x,y)
            
        elif var_1 == int(6):
            print("You're doing Modules of x")
            x = float(input("Press x: "))
            y = float(input("Press y: "))
            modulus(x,y)
        elif var_1 == int(101):
            exit()   
    #####################################################Fourth UI
    elif choose_first == int(2):
        print("""
0:(a+b)²=a²+b²+2ab
1:(a-b)²=a²+b²-2ab
2:a²+b²=(a+b)²-2ab
3:a²-b²=(a+b)*(a-b)
4:a³+b³=(a+b)*(a²-ab+b²)=(a+b)³-3ab*(a+b)
5:a³-b³=(a-b)*(a²+ab+b²)=(a-b)³+3ab*(a-b)
6:2(a²+b²)=(a+b)²+(a-b)²
7:(a+b)²-(a-b)²=4ab
8:a^4+b^4=(a+b)(a-b)[(a+b)²-2ab]
9:(a+b+c)²=a²+b²+c²+2ab+2bc+2ca
10:(a+b-c)²=a²+b²+c²+2ab-2bc-2ca
11:(a-b-c)²=a²+b²+c²-2ab-2bc-2ca
Type 101 to exit 

        """)
        var = int(input("Enter the number of operation you want to do  : "))
        if var == int(0):
            print("You're doing (a+b)²=a²+b²+2ab ")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            one(a,b)
            
        elif var == int(1):
            print("You're doing (a-b)²=a²+b²-2ab ")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            two(a,b)
            
        elif var == int(2):
            print("You're doing a²+b²=(a+b)²-2ab ")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            three(a,b)
            
        elif var == int(3):
            print("You're doing a²-b²=(a+b)*(a-b)")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            four(a,b)
            
        elif var == int(4):
            print("You're doing a³+b³=(a+b)*(a²-ab+b²)=(a+b)³-3ab*(a+b)")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            five(a,b)
            
        elif var == int(5):
            print("You're doing a³-b³=(a-b)*(a²+ab+b²)=(a-b)³+3ab*(a-b)")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            six(a,b)
            
        elif var == int(6):
            print("You're doing 2(a²+b²)=(a+b)²+(a-b)²")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            seven(a,b)
            
        elif var == int(7):
            print("You're doing (a+b)²-(a-b)²= 4ab")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            eight(a,b)
            
        elif var == int(8):
            print("You're doing a^4+b^4=(a+b)(a-b)[(a+b)²-2ab]")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            nine(a,b)
            
        elif var == int(9):
            print("You're doing (a+b+c)²=a²+b²+c²+2ab+2bc+2ca")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            c = float(input("Press c "))
            ten(a,b,c)
            
        elif var == int(10):
            print("You're doing (a+b-c)²=a²+b²+c²+2ab-2bc-2ca")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            c = float(input("Press c "))
            eleven(a,b,c)
            
        elif var == int(11):
            print("You're doing (a-b-c)²=a²+b²+c²-2ab-2bc-2ca")
            a = float(input("Press a: "))
            b = float(input("Press b: "))
            c = float(input("Press c "))
            twelve(a,b,c)
        elif var == int(101):
            exit()
###############################################################################
    elif choose_first == int(3): 
        print("""
1:Round after 1 decimal places
2:Round after 2 decimal places
3:Round after 3 decimal places
4:Round to nearest 10 
5:Round to nearest 100
6:round to nearest 1000
Type 101 to exit  
        """)
        var = int(input("Enter the number of operation you want to do: "))
        if var == int(1):
            a = float(input("Enter the number: "))
            print(round(a, 1))
            
        elif var == int(2):
            a = float(input("Enter the number: "))
            print(round(a, 2))
            
        elif var == int(3):
            a = float(input("Enter the number: "))
            print(round(a, 3))
            
        elif var == int(4):
            a = float(input("Enter the number: "))
            print(round(a, -1))
            
        elif var == int(5):
            a = float(input("Enter the number: "))
            print(round(a, -2)) 
               
        elif var == int(6):
            a = float(input("Enter the number: "))
            print(round(a, -3))
            
        elif var == int(101):
            exit()
################### 
    elif choose_first == int(4):
        list_of_numbers = list(map(int, input("Type the numbers separetated by space:").split()))
        print(f"The mean of the numbers is {sum(list_of_numbers)/len(list_of_numbers)}")
###################       
    elif choose_first == int(5):
        list_of_numbers = list(map(int, input("Enter the numbers separeted by space:").split()))
        m = max(list_of_numbers)
        l = min(list_of_numbers)
        print(f"The range is {m-l}")
###################
    elif choose_first == int(6):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the power number: "))
        power(a,b)
####################
    elif choose_first == int(7):
        print("""
1:Finding the percentage        
2:Increase the percentage
3:Decrease the percentage
4:Find the difference between the numbers in %
5:Compound interest 
Type 101 to exit      
        """)
        var = int(input("Enter the number of operation you want to do: "))
        if var == int(1):
            a = float(input("Enter the number: "))
            b = float(input("Enter the percentage: "))
            found_the_procent(a,b)
        elif var == int(2):
            a = float(input("Enter the number: "))
            b = float(input("Enter the percentage: "))
            percentage_increase(a,b)
        elif var == int(3):
            a = float(input("Enter the number: "))
            b = float(input("Enter the percentage: "))
            percentage_decrease(a,b)
        elif var == int(4):
            a = float(input("Enter the first number: "))
            b = float(input("Enter the last number: "))
            percentage_difference(a,b)
        elif var == int(5):
            a = float(input("Enter  future value of the investment/loan£: "))
            b = float(input("Enter the annual interest rate%: "))
            c = int(input("Enter the number of times that interest is compounded per year: "))
            compound_interes(a,b,c)

        elif var == int(101):
            exit()
#####################
    elif choose_first == int(8):
        print("""
1:mm to cm,dm,m,km
2:cm to mm,dm,m,km
3:dm to mm,cm,m,km
4:m to mm,cm,dm,km
5:km to mm,cm,dm,m
Type 101 to exit
        """)
        var = int(input("Enter the number of operation you want to do:"))
        if var == int(1):
            a = float(input("Enter the  number in mm: "))
            mm(a)
        elif var == int(2):
            a = float(input("Enter the number in cm: "))
            cm(a)
        elif var == int(3):
            a = float(input("Enter the number in dm: "))
            dm(a)
        elif var == int(4):
            a = float(input("Enter the number in m: "))
            metre(a)
        elif var == int(5):
            a = float(input("Enter the number in km: "))
            km(a)
        elif var == int(101):
            exit()
    elif choose_first == int(9):
        my_mode()
    elif choose_first == int(10):
        print("""
1:Line Graphs
2:Bar Chart
3:Pie Charts
""")
        var = int(input("Enter the number of operation:"))
        if var == int(1):
            line_graphs()
        elif var == int(2):
            bar_chart()
        elif var == int(3):
            pie_chart()

        
    elif choose_first == int(101):
        exit()


project_app()   