class Employee:
    a = 1  # Class attribute

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self): 
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# Creating an instance of Employee
e = Employee()

# Instance attribute (this creates a new attribute for the instance, not modifying the class variable)
e.a = 45  

# Setting name (using the setter method)
e.name = "Harry Khan"

# Getting name (using the getter method)
print(e.name)  # Output: Harry Khan

# Calling class method
e.show()  # Output: The class attribute of a is 1
