import pylab
import math

# Reference: program 2-28, program D-1, program 5-4

def plot_function(fun_str, d, n):

    #empty list for x and y
    xaxis = []   
    yaxis = []
    
    # gets min and max values
    (xmin, xmax) = d
    #calculates the distance 
    ds = (xmax - xmin) / (n - 1)

    #loops through number of samples
    i = 0
    for i in range(0, n):
        x = xmin + i * ds # gets current x value
        xaxis.append(x) # adds x value
        y = eval(fun_str) # uses fuction to get y
        yaxis.append(y) # adds y value

        print(x, y) # prints values

    # plots the x and y values and title and displays graph
    pylab.plot(xaxis, yaxis)
    pylab.title("2 * math.sin(2*math.pi * x)")
    pylab.show()



fun_str = input("Enter function with variable x: ") # asks user to enter variable
n = float(input("Enter number of samples: ")) # asks user to enter samples
xmin = float(input("Enter xminimum: ")) # asks user to enter min
xmax = float(input("Enter xmaximum: ")) # asks user to enter max

plot_function(fun_str, (xmin, xmax), n) # creates graph 