#Problem 4
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.

    Returns b.
    """
    #checks if it worked
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


#adds text to the end of the file
#Reference: W3Schools, python file handling and file write
def ed_append(filename: str, string: str) -> int:
    """Append a string to a file."""
    with open(filename, "a") as f:
        return f.write(string)


#read the file, can also read just part of it
#Reference: W3Schools, python file handling and string slicing
def ed_read(filename: str, start: int = 0, to: int = -1) -> str:
    """Read part of a file."""
    with open(filename, "r") as f:
        text = f.read()

    if to == -1:
        return text[start:]

    #make sure the ending position is valid
    if to > len(text):
        raise IndexError("end of file")

    return text[start:to]


#finds where a string shows up in the file
#Reference: W3Schools, python string methods and while loops
def ed_find(filename: str, search_str: str) -> list[int]:
    """Find all positions of a string in a file."""
    with open(filename, "r") as f:
        text = f.read()

    positions = []
    index = text.find(search_str)

    #keeps going until there are no more matches
    while index != -1:
        positions.append(index)
        index = text.find(search_str, index + 1)

    return positions


#replace text in the file
#Reference: W3Schools, python string methods
def ed_replace(filename: str, search_str: str, replace_with: str,
               occurrence: int = -1) -> int:
    """replace a string in a file and return the number of replacements."""
    with open(filename, "r") as f:
        text = f.read()

    #-1 means replace all of them
    if occurrence == -1:
        count = text.count(search_str)
        new_text = text.replace(search_str, replace_with)
    else:
        positions = ed_find(filename, search_str)

        #nothing to replace if that occurrence isn't there
        if occurrence >= len(positions):
            return 0

        #only change the chosen match
        pos = positions[occurrence]
        new_text = text[:pos] + replace_with + text[pos + len(search_str):]
        count = 1

    if count > 0:
        with open(filename, "w") as f:
            f.write(new_text)

    return count


#resets the file with the test numbers
#Reference: W3Schools, python file write
def reset_file(filename: str) -> None:
    """writes the test content to a file"""
    with open(filename, "w") as f:
        f.write("01234567890123456789")


#tests the find function
# Reference: Chapter 12
def try_ed_find() -> None:
    """test the ed_find function"""
    fn = "test_file.txt"

    #resets the file before starting the tests
    reset_file(fn)

    #checks if it finds both matches and returns 
    testif(ed_find(fn, "345") == [3, 13], "find two matches")

    #checks what happens when the text is not found
    testif(ed_find(fn, "356") == [], "find no match")

    #checks if it finds the number 9 in both places
    testif(ed_find(fn, "9") == [9, 19], "find a single character")


#tests the replace function using testif
#Reference: Chapter 12, homework 3 problems 1-2
def try_ed_replace() -> None:
    """test the ed_replace function"""
    fn = "test_file.txt"

    #reset the file before testing the second match
    reset_file(fn)

    #checks if the second match was replaced and returned 1
    testif(ed_replace(fn, "345", "ABCDE", 1) == 1,
           "replace second - return value")

    #checks if the file has the new text in the right spot
    testif(ed_read(fn) == "0123456789012ABCDE6789",
           "replace second - file")

    #reset the file to test replacing every match
    reset_file(fn)

    #checks if both matches were replaced
    testif(ed_replace(fn, "345", "ABCDE") == 2,
           "replace all: return value")

    #checks if both changes show up in the file
    testif(ed_read(fn) == "012ABCDE6789012ABCDE6789",
           "replace file")

    #reset the file again for a match that does not exist
    reset_file(fn)

    #checks that it returns 0 if the occurrence is missing
    testif(ed_replace(fn, "345", "ABCDE", 5) == 0,
           "missing occurrence - return value")

    #makes sure the file stays the same when nothing is replaced
    testif(ed_read(fn) == "01234567890123456789",
           "missing occurrence - file unchanged")

#main part of the program
#Reference: Chapter 13, homework 3 problems 1-2
def main() -> None:
    """shows the functions and run the tests"""
    fn = "file1.txt"

    #start with an empty file
    with open(fn, "w") as f:
        pass

    #add some numbers
    print(ed_append(fn, "0123456789"))
    print(ed_append(fn, "0123456789"))

    #read different parts
    print(ed_read(fn, 3, 9))
    print(ed_read(fn, 3))

    #try finding strings
    print(ed_find(fn, "345"))
    print(ed_find(fn, "356"))

    #replace the second match
    print(ed_replace(fn, "345", "ABCDE", 1))
    print(ed_read(fn))

    #clear the file again
    with open(fn, "w") as f:
        pass

    ed_append(fn, "0123456789")
    ed_append(fn, "0123456789")

    #replace all matches this time
    print(ed_replace(fn, "345", "ABCDE"))
    print(ed_read(fn))

    #run the tests at the end
    try_ed_find()
    try_ed_replace()


if __name__ == "__main__":
    main()


# References:
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_strings.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/ref_string_find.asp
# https://www.w3schools.com/python/ref_string_count.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# Also used Chapters 12-13 and homework 3 problems 1-2