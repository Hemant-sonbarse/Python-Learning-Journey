'''
4. Write a class 'Complex' to represent complex numbers, along with overloaded
operators '+' and '*' which adds and multiplies them.
'''


class Complex:
    def __init__(self, real, imag):  # ✅ Clearer variable names
        self.real = real   # Real part of the complex number
        self.imag = imag   # Imaginary part of the complex number

    def __add__(self, other):  # ✅ Overloading `+` for addition
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def __mul__(self, other):  # ✅ Overloading `*` for multiplication
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex(new_real, new_imag)

    def __str__(self):  # ✅ Overloading str() for proper output
        return f"{self.real} + {self.imag}i"

# ✅ Creating Complex Numbers
num1 = Complex(1, 2)  # 1 + 2i
num2 = Complex(3, 4)  # 3 + 4i

# ✅ Adding Complex Numbers
sum_result = num1 + num2  # (1+3) + (2+4)i = 4 + 6i
print("Addition:", sum_result)  # Output: 4 + 6i

# ✅ Multiplying Complex Numbers
product_result = num1 * num2  # (1*3 - 2*4) + (1*4 + 2*3)i = -5 + 10i
print("Multiplication:", product_result)  # Output: -5 + 10i
