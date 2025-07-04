'''
5. Write a class vector representing a vector of n dimensions. Overload the + and *
operator which calculates the sum and the dot(.) product of them.
'''

class Vector:
    def __init__(self, x, y, z):
        """Initialize a 3D vector with x, y, and z components."""
        self.x = x  # Store x-coordinate
        self.y = y  # Store y-coordinate
        self.z = z  # Store z-coordinate

    def __add__(self, other):
        """Overload + to add two vectors component-wise."""
        new_x = self.x + other.x  # Add x components
        new_y = self.y + other.y  # Add y components
        new_z = self.z + other.z  # Add z components
        return Vector(new_x, new_y, new_z)  # Return a new vector

    def __mul__(self, other):
        """Overload * to calculate the dot product."""
        dot_product = (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        return dot_product  # Returns a single number (scalar)

    def __str__(self):
        """Return a string representation of the vector."""
        return f"Vector({self.x}, {self.y}, {self.z})"

# ✅ Creating Vectors
vector1 = Vector(1, 2, 3)  # Vector (1, 2, 3)
vector2 = Vector(4, 5, 6)  # Vector (4, 5, 6)

# ✅ Adding Vectors
sum_vector = vector1 + vector2  # (1+4, 2+5, 3+6) = (5, 7, 9)
print("Sum:", sum_vector)  # Output: Vector(5, 7, 9)

# ✅ Dot Product of Vectors
dot_product = vector1 * vector2  # (1*4 + 2*5 + 3*6) = 32
print("Dot Product:", dot_product)  # Output: 32
