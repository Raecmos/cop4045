#Problem 1 
# Provided by professor 
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false
    otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b


#Reference - Chapter 11.1
#Reference - W3Schools: python classes and objects
class NVector:
    """ class that implements an n real vector"""

    # A and B - Constructor
    # A: accepts one sequence argument and copies its elements into a new list
    # B: accepts two or more arguments and uses them as the vector elements
    #Reference - chapter 11.1
    def __init__(self, *args) -> None:
        """construcor with a variable number of arguments"""

        #checks if there is one argument
        #Reference - chapter 12.1
        if len(args) == 1:
            #makes the argument into a list
            #Reference -Chapter 11.8
            self.__data = list(args[0])

        #checks if there is more than one argument
        #Reference - chapter 12.1
        elif len(args) > 1:
            #puts the arguments into a list
            self.__data = list(args)

        #gives an error if there are no arguments
        #Reference - chapter 12.1
        else:
            raise ValueError("needs one argument ")

        #saves the number of values
        #Reference - chapter 11.1
        self.dim = len(self.__data)

    # C - returns the length of the vector
    #Reference - W3Schools: Python len() function
    def __len__(self) -> int:
        return self.dim

    # D - allows getting a value using its index
    #Reference - chapter 11.1
    def __getitem__(self, index: int):
        return self.__data[index]

    # E - allows changing a value using its index
    #Reference - chapter 11.3
    def __setitem__(self, index: int, val) -> None:
        self.__data[index] = val

    # F - shows the vector as a string
    #Reference - Chapter 11.6
    def __str__(self) -> str:
        return str(self.__data)

    #gives the vector a string representation
    #Reference - Chapter 12.3
    def __repr__(self) -> str:
        return str(self)

    # G - checks if two vectors are equal or not
    #Reference - chapter 12.7
    def __eq__(self, other: object) -> bool:
        #checks if the other object is a vector
        if not isinstance(other, NVector):
            return False
        return self.__data == other.__data

    #checks if two vectors are different
    #Reference - chapter 12.7
    def __ne__(self, other: object) -> bool:
        return not (self == other)

    # H - adds two vectors or adds a number to each value
    #Reference - Chapter 12.2
    #Reference - GeeksforGeeks: operator overloading in Python
    def __add__(self, other) -> "NVector":
        #checks if the other object is a vector
        #Reference - chapter 12.8
        if isinstance(other, NVector):
            #checks if the vectors are the same length
            if len(self) != len(other):
             raise ValueError("wrong vector length")

            #adds the values at the same positions
            return NVector([self.__data[i] + other.__data[i]
                           for i in range(len(self))])
        else:
            #adds the number to every value
            return NVector([self.__data[i] + other
                         for i in range(len(self))])

    #allows the number to be on the left side
    #Reference - chapter 12.9
    def __radd__(self, other) -> "NVector":
        return self + other

    # I - multiplies two vectors or multiplies each value by a number
    #Reference - GeeksforGeeks: operator overloading in Python
    def __mul__(self, other):
        #checks if the other object is a vector
        if isinstance(other, NVector):
            #checks if the vectors are the same length
            if len(self) != len(other):
                raise ValueError("wrong vector length")

            #multiplies the matching values and adds them together
            return sum([self.__data[i] * other.__data[i]
                for i in range(len(self))])
        else:
            #multiplies each value by the number and adds them
            return sum([self.__data[i] * other
                for i in range(len(self))])

    #allows the number to be on the left side
    #Reference - GeeksforGeeks: operator overloading in Python
    def __rmul__(self, other):
        return self * other

    # J - creates a new vector with n zeros
    #Reference - Chapter 11.1
    @classmethod
    def zeros(cls, n):
        return cls([0] * n)


# K - tests the NVector methods from parts A - I
#Reference - chapter 13.7
#Reference - recursion examples
def main() -> None:
    #makes a vector with four values
    v = NVector(3, 0, 1, -1)

    #checks the length
    #Reference - Recursion examples
    testif(len(v) == 4, "length")

    #checks the value at index 1
    testif(v[1] == 0, "getitem")

    #checks if negative indexes work
    testif(v[-2] == 1, "negative getitem")

    #changes the value at index 2
    v[2] = 5

    #checks if the value changed
    testif(v[2] == 5, "setitem")

    #checks if two vectors can be added
    #Reference - Chapter 12.2
    testif(NVector(3, 0, 1, -1) + NVector(1, 2, 3, 4)
         == NVector(4, 2, 4, 3), "add NVector")

    #checks if two vectors can be multiplied
    testif(NVector(3, 0, 1, -1) * NVector(1, 2, 3, 4)
        == 3 * 1 + 0 * 2 + 1 * 3 + (-1) * 4, "multi NVector")

    #checks if a list works in the constructor
    #Reference - W3Schools: Python classes and objects
    testif(NVector([3, 0, 1, -1])[0] == 3, "const list")

    #checks if a tuple works in the constructor
    testif(NVector((3, 0, 1, -1))[3] == -1, "const tuple")

    #checks how the vector looks as a string
    #Reference - Chapter 11.6
    testif(str(v) == "[3, 0, 5, -1]", "str")

    #checks if two matching vectors are equal
    #Reference - Chapter 12.7
    testif(NVector(1, 2) == NVector([1, 2]), "eq")

    #checks if two different vectors are not equal
    testif(NVector(1, 2) != NVector(1, 3), "ne")

    #checks if a vector is not equal to a number
    testif(not (NVector(1, 2) == 5), "non NVector eq")

    #checks if a number can be added to every value
    #Reference - Chapter 12.6
    testif(NVector(3, 0, 1, -1) + 10 == NVector(13, 10, 11, 9), "add number")

    #checks if addition works with the number on the left
    #Reference - Chapter 12.9
    testif(10 + NVector(3, 0, 1, -1) == NVector(13, 10, 11, 9), "radd number")

    #checks if each value can be multiplied by a number
    testif(NVector(3, 0, 1, -1) * 10 == 3 * 10 + 0 * 10 + 1 * 10 + (-1) * 10, "multi number")

    #checks if multiplication works with the number on the left
    testif(10 * NVector(3, 0, 1, -1) == 3 * 10 + 0 * 10 + 1 * 10 + (-1) * 10, "re-multi number")

    #checks if zeros makes a vector of zeros
    testif(NVector.zeros(3) == NVector(0, 0, 0), "zeros")

    #checks if an invalid index gives an error
    #Reference - W3Schools: Python try and except
    try:
        x = v[20]
    except IndexError:
        testif(True, "getitem wrong index")
    else:
        testif(False, "getitem wrong index")

    #checks if changing an invalid index gives an error
    try:
        v[20] = 1
    except IndexError:
        testif(True, "setitem wrong index")
    else:
        testif(False, "setitem wrong index")

    #checks if a number causes an error in the constructor
    try:
        x = NVector(5)
    except TypeError:
        testif(True, "constructor with a scalar")
    else:
        testif(False, "constructor with a scalar")


if __name__ == "__main__":
    main()


#References : https://www.w3schools.com/python/python_try_except.asp, https://www.w3schools.com/python/python_classes.asp, #https://www.geeksforgeeks.org/operator-overloading-in-python/,
#Reference continued ; #https://www.w3schools.com/python/ref_func_len.asp and Chapters 11-12.