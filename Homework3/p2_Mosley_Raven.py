#Problem 2

#Reference - W3Schools: Python Classes and Objects
class ParkingPermit:
    """A class for a parking permit."""

    #Reference - Chapter 11.1
    def __init__(self, owner: str, months: int, fees: dict[str, float]) -> None:
        """Sets up the owner, months, and fees."""
        #stores the permit information
        self._owner = owner
        self._months = months
        self._fees = fees

    #Reference - chapter 11.1
    def owner(self) -> str:
       #returns the owner's name
        return self._owner

    #Reference - chapter 11.1
    def months(self) -> int:
        #returns the number of months
        return self._months

    #Reference - W3Schools: Python Dictionaries
    def fees(self) -> dict[str, float]:
        #returns the fee information
        return self._fees

    #Reference - Chapter 11.6
    def __str__(self) -> str:
        #returns the permit information as a string
        #shows the owner, months, and cost
        return "{}, {} months, ${}".format(self.owner(), self.months(), self.cost())

    #calculates the regular permit cost
    def cost(self) -> float:
        #calculates the regular permit cost
        return self._months * self._fees["monthly"]

    #Reference - Chapter 12.3
    def __repr__(self) -> str:
        #returns a string showing how the object was created
        return "{}({}, {})".format(type(self).__name__, self._owner, self._months)


#Reference - W3Schools: Python Inheritance
class StudentPermit(ParkingPermit):

    """A parking permit for students."""

    def __init__(self, owner: str, months: int, fees: dict[str, float], vehicles: int) -> None:
        """Sets up the student permit and number of vehicles."""

        #Reference - GeeksforGeeks: Python super()
        #calls the constructor from the parent class
        super().__init__(owner, months, fees)
        self._vehicles = vehicles

    #Reference - GeeksforGeeks: Inheritance in Python method overriding
    def cost(self) -> float:
        """Calculates the student permit cost."""
        #figures out how many extra vehicles there are
        extra = max(self._vehicles - 1, 0)
        return super().cost() + extra * self._fees["cost"]


#Reference - W3Schools: Python Inheritance
class FacultyPermit(ParkingPermit):

    """A parking permit for faculty."""

    def __init__(self, owner: str, months: int, fees: dict[str, float], garage: bool) -> None:
        """Sets up the faculty permit and garage access."""

        #Reference - GeeksforGeeks: Python super
        #calls the constructor from the parent class
        super().__init__(owner, months, fees)
        self._garage = garage

    #Reference - GeeksforGeeks: Inheritance in Python method overriding
    def cost(self) -> float:
        """Calculates the faculty permit cost."""
        #starts with the regular permit cost
        total = super().cost()

        #adds the garage fee if garage access is included
        if self._garage:
            total += self._months * self._fees["garage"]
        return total


def summarize_list(permits: list[ParkingPermit]) -> float:
    """Prints each permit and returns the total revenue."""
    total = 0.0

    #Reference - W3Schools: Python For Loops
    #goes through each permit in the list
    for permit in permits:
        print(permit)
        total += permit.cost()
    return total


#Reference - chapter 13.7
def main() -> None:
    """Creates permits and shows how they work."""

    #sets the fees for each type of permit
    student_fees = {"monthly": 25, "cost": 10}
    faculty_fees = {"monthly": 40, "garage": 15}

    #creates the student and faculty permits
    student1 = StudentPermit("Student 1", 2, student_fees, 1)
    student2 = StudentPermit("Student 2", 3, student_fees, 2)
    faculty1 = FacultyPermit("Professor Lunk", 3, faculty_fees, True)
    faculty2 = FacultyPermit("Professor Steam", 2, faculty_fees, False)

    #prints each permit
    print(student1)
    print(student2)
    print(faculty1)
    print(faculty2)

    #puts all permits into one list
    permits = [student1, student2, faculty1, faculty2]
    total = summarize_list(permits)

    #prints the total revenue
    print(total)


if __name__ == "__main__":
    main()

#References : https://www.w3schools.com/python/python_classes.asp, https://www.w3schools.com/python/python_inheritance.asp, https://www.w3schools.com/python/python_dictionaries.asp,
#https://www.w3schools.com/python/python_for_loops.asp, https://www.geeksforgeeks.org/python-super/, https://www.geeksforgeeks.org/inheritance-in-python/,
#Reference continued ; Chapters 11-13.