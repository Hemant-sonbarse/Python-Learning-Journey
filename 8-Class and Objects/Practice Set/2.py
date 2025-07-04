'''
2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from
'Pets'. Add a method 'bark' to class 'Dog'.
'''


class Animals:
    pass  # Empty class

class Pets(Animals):
    pass  # Inherits from Animals

class Dog(Pets):  # Inherits from Pets
    @staticmethod
    def bark():
        print("Bow Bow!")

# ✅ Correct way to create an object
d = Dog()  # Create an instance of Dog
d.bark()   # Output: Bow Bow!

# ✅ You can also call the static method directly from the class
Dog.bark()  # Output: Bow Bow!



'''
Without @staticmethod 

class Dog:
    def bark(self):  # Needs 'self' (object)
        print("Bow Bow!")

d = Dog()  # Create object
d.bark()  # ✅ Works fine
Dog.bark()  # ❌ Error (Needs an object)
'''