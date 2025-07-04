#1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):  # Fixed constructor (__init__)
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):  # Inherit from TwoDVector
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Corrected super() call
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# Creating objects
a = TwoDVector(1, 2)
a.show()  # Output: The vector is 1i + 2j

b = ThreeDVector(1, 2, 3)
b.show()  # Output: The vector is 1i + 2j + 3k
