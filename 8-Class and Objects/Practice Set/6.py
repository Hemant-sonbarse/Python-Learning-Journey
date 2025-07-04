'''
6. Write_str_() method to print the vector as follows:
7i + 8j +10k
Assume vector of dimension 3 for this problem.
'''

class Vector:
    def __init__(self, x, y, z):
        """Initialize a 3D vector with x, y, and z components."""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Overload + to add two vectors component-wise."""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        """Overload * to calculate the dot product."""
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

#just modified this and overall code is same as 5
    def __str__(self):
        """Return the vector in the format: 7i + 8j + 10k"""
        return f"{self.x}i + {self.y}j + {self.z}k"

# ✅ Creating Vectors
v1 = Vector(7, 8, 10)
v2 = Vector(1, 2, 3)

# ✅ Printing Vectors
print("Vector 1:", v1)  # Output: 7i + 8j + 10k
print("Vector 2:", v2)  # Output: 1i + 2j + 3k

# ✅ Adding Vectors
sum_vector = v1 + v2  # (7+1)i + (8+2)j + (10+3)k = 8i + 10j + 13k
print("Sum:", sum_vector)  # Output: 8i + 10j + 13k

# ✅ Dot Product of Vectors
dot_product = v1 * v2  # (7*1) + (8*2) + (10*3) = 7 + 16 + 30 = 53
print("Dot Product:", dot_product)  # Output: 53
