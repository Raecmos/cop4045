import matplotlib.pyplot as plt
import numpy as np

# Reference: program 3-5, program 5-4, chapters 1-5

# keeps asking for values until user quits
while True:

    # gets the a, b, and c values from user
    a_str = float(input ("Enter a: "))
    b_str = float(input ("Enter b: "))
    c_str = float(input ("Enter c: "))

    # checks if the user enters nothing c
    if (a_str, b_str, c_str) == "": 
        break

    # gets the discriminant
    d_str = b_str * b_str - 4 * a_str * c_str

    # if discriminant is negative theres no real solutions
    if d_str < 0:
        print ("no real solutions")

    # if the discriminant is zero theres one solution
    elif d_str == 0:
        x = -b_str/(2*a_str)
        print("one solution: ", x)

    # otherwise theres two solutions
    else:
        sqrtd = np.sqrt(d_str)
        x1 = (-b_str - sqrtd)/(2*a_str)
        x2 = (-b_str + sqrtd)/(2*a_str)
        print("two solutions: ", x1, " and ", x2) # prints both solution
