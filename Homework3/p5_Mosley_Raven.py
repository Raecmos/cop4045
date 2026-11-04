#Problem 5
from turtle import *

#test function from homework 3
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. Returns b."""
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


#part a - recursive leaf
#Reference: class snowflake example
def draw_leaf_straight(level: int, length: int) -> None:
    """draws a straight leaf using recursion"""

    #helper function for the branches
    def branch(size, depth):
        """draws the smaller parts of the leaf"""

        if depth == 0:
            return
        #draw part of the middle stem
        forward(size / 2)

        #left branch
        left(45)
        branch(size / 2, depth - 1)
        right(45)

        #right branch
        right(45)
        branch(size / 2, depth - 1)
        left(45)

        #continue up the middle
        forward(size / 2)
        branch(size / 2, depth - 1)

        #go back to where it started
        backward(size)

    clearscreen()
    delay(0)
    speed(0)
    color("black")

    up()
    goto(0, -250)
    setheading(90)
    down()

    #lower part of the stem
    forward(length)

    #draw the leaf
    branch(length, level)


#part b - base conversion
#Reference: class recursive_sum example
#Reference: W3Schools, python recursion and strings
def strB(n: int, base: int = 10) -> str:
    """converts a number to a string in another base"""

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #base case
    if n < base:
        return digits[n]
    else:
        #keeps converting the remaining number
        return strB(n // base, base) + digits[n % base]


#tests for strB
#Reference: homework 3 testif function
#checks if 25 converts to binary correctly
testif(strB(25, 2) == "11001", "binary")

#checks if 255 converts to base 16
testif(strB(255, 16) == "FF", "hex")

#tests converting 50 to base 8
testif(strB(50, 8) == "62", "octal")

#checks if the function works when number is 0
testif(strB(0) == "0", "zero")


#part c - binomial coefficient
#Reference: class ack_memoized and hanoi examples
def Cnk_m(n: int, k: int) -> int:
    """calculates n choose k using recursion and memoization"""

    #checks if the answer is already saved
    if (n, k) not in Cnk_dct:

        #base case
        if k == 0 or k == n:
            ret = 1
        else:
            #calculates the two smaller values
            ret = Cnk_m(n - 1, k - 1) + Cnk_m(n - 1, k)

        #saves the answer
        Cnk_dct[(n, k)] = ret

    return Cnk_dct[(n, k)]


#dictionary for memoization
Cnk_dct = {}

#tests for Cnk_m
#Reference: homework 3 testif function
#checks if choosing 2 from 5 gives 10
testif(Cnk_m(5, 2) == 10, "choose 5 2")

#checks if choosing 3 from 6 returns 20
testif(Cnk_m(6, 3) == 20, "choose 6 3")

#tests base when k is 0
testif(Cnk_m(10, 0) == 1, "choose 10 0")

#checks if choosing 4 from 8 gives 70
testif(Cnk_m(8, 4) == 70, "choose 8 4")


#used to show results in the python 
#Reference: class ack_memoized example
def run_Cnk() -> None:
    """prints some binomial coefficient results"""

    #calculates choosing 3 from 10
    print("Cnk(10, 3) =", Cnk_m(10, 3))

    #checks the result of choosing 5 from 12
    print("Cnk(12, 5) =", Cnk_m(12, 5))

    #calculates choosing 7 from 15
    print("Cnk(15, 7) =", Cnk_m(15, 7))


#part d - making pairs
#Reference: class recursive_sum_acc and list_range_acc
def make_pairs(seq1: list, seq2: list, acc=None) -> list:
    """makes pairs from two lists using recursion"""

    if acc is None:
        acc = []

    #stops when one list is empty
    if len(seq1) == 0 or len(seq2) == 0:
        return acc
    else:
        #adds the pair and go to the next items
        return make_pairs(seq1[1:], seq2[1:], acc + [(seq1[0], seq2[0])])


#tests for make_pairs
testif(make_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)], "two pairs")

testif(make_pairs([1, 2, 3], [4]) == [(1, 4)], "shorter second list")

testif(make_pairs([], [1, 2]) == [], "empty first list")

testif(make_pairs([1, 2], []) == [], "empty second list")

testif(make_pairs([5], [8]) == [(5, 8)], "one pair")


#draw the leaf for the screenshot
draw_leaf_straight(6, 120)
done()


#References:
#class snowflake recursion example
#class recursive_sum example
#class recursive_sum_acc and list_range_acc examples
#class ack_memoized example
#class hanoi example
#homework 3 testif function
#https://www.w3schools.com/python/python_recursion.asp
#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/python_strings.asp
#https://docs.python.org/3/library/turtle.html
