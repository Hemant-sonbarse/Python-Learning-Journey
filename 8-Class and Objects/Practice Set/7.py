#7. Override the_len_() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, x, y, z):
        """Initialize a 3D vector with x, y, and z components."""
        self.x = x  # Store x-coordinate
        self.y = y  # Store y-coordinate
        self.z = z  # Store z-coordinate

    def __add__(self, other):
        """Overload + to add two vectors component-wise."""
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        """Overload * to calculate the dot product."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        """Return a string representation of the vector."""
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __len__(self):
        """Return the dimension of the vector (always 3 for 3D vectors)."""
        return 3

# ✅ Test the implementation
v1 = Vector(1, 2, 3)  # Corrected initialization
v2 = Vector(4, 5, 6)

print("Vector 1:", v1)  # Output: 1i + 2j + 3k
print("Vector 2:", v2)  # Output: 4i + 5j + 6k

# ✅ Testing Addition
sum_vector = v1 + v2  # (1+4)i + (2+5)j + (3+6)k = 5i + 7j + 9k
print("Sum:", sum_vector)  # Output: 5i + 7j + 9k

# ✅ Testing Dot Product
dot_product = v1 * v2  # (1*4 + 2*5 + 3*6) = 32
print("Dot Product:", dot_product)  # Output: 32

# ✅ Checking Vector Dimension
print("Dimension of Vector:", len(v1))  # Output: 3
