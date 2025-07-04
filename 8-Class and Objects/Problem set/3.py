'''
3. Create a class with a class attribute a; create an object from it and set 'a'
directly using object.a = 0. Does this change the class attribute?
'''

class Demo:
    a = 4  # Class attribute

# Create an object of Demo
o = Demo()
print(o.a)  # Prints the class attribute (4) because no instance attribute is set yet

# Assign a new value to 'a' for the object 'o'
o.a = 0  # This creates a new instance attribute 'a' for object 'o'
print(o.a)  # Prints the instance attribute (0)

# Print the class attribute to check if it changed
print(Demo.a)  # Prints the class attribute (4), proving it remains unchanged





#The class attribute doesnt change 